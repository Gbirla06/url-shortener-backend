from datetime import datetime
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
import httpx
import shortuuid
from app.database import urls_collection
from app.schema import URLSchema


router = APIRouter()

async def is_url_reachable(url: str) -> bool:
    """
    Check if the provided URL is reachable by making a HEAD request.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is reachable (status code < 400), False otherwise.
    """
    try:
        response = httpx.get(url, timeout=5, follow_redirects=True)  # ✅ Change HEAD → GET
        return response.status_code < 400
    except httpx.RequestError:
        return False



@router.post("/shorten")
async def shorten_url(inData: URLSchema):
    """
    Shorten a given long URL.

    Args:
        inData (URLSchema): The input data containing the long URL.

    Returns:
        dict: A dictionary containing the short URL and the total number of clicks.
    """
    long_url = str(inData.long_url)
    existing_url = await urls_collection.find_one({"long_url": long_url})

    if existing_url:
        return {"short_url": existing_url["_id"], "total_clicks": existing_url['clicks']}

    if not await is_url_reachable(long_url):
        raise HTTPException(status_code=400, detail="Invalid URL provided")

    short_code = shortuuid.ShortUUID().random(length=10)

    await urls_collection.insert_one({
        "_id": short_code,
        "long_url": long_url,
        "created_at": datetime.now(),
        "clicks": 0
    })

    return {"short_url": short_code, "total_clicks": 0}



@router.get("/{short_code}")
async def redirect(short_code: str):
    """
    Redirect to the original long URL based on the provided short code.

    Args:
        short_code (str): The short code of the URL.

    Returns:
        RedirectResponse: A response that redirects to the long URL.
    """
    url_data =  await urls_collection.find_one({"_id": short_code})

    if not url_data:
        raise HTTPException(status_code=404, detail="Short URL not found")

    await urls_collection.update_one(
        {"_id": short_code},
        {"$inc": {"clicks": 1}}
    )
    return RedirectResponse(url=url_data["long_url"])

