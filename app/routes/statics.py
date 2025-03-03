from fastapi import APIRouter, HTTPException
from app.database import urls_collection

router = APIRouter()

@router.get("/urls-data")
async def statics_about_urls():
    """
    Retrieve statistics about all shortened URLs.

    Returns:
        list: A list of dictionaries containing the short URL, number of clicks, and the long URL.
    """
    all_urls_cursor = urls_collection.find({})  # Returns a cursor
    all_urls = await all_urls_cursor.to_list(length=None)  # Fetch all results

    all_urls_data = []
    for url in all_urls:
        all_urls_data.append({
            'short_url' : str(url['_id']),
            'clicks' : url.get('clicks', 0),
            'long_url' : url['long_url']
        })
    return all_urls_data