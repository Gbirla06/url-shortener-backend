from fastapi import APIRouter, HTTPException
from app.database import urls_collection

router = APIRouter()


@router.get("/urls-data")
def statics_about_urls():
    all_urls = urls_collection.find({})

    all_urls_data = []
    for url in all_urls:
        all_urls_data.append({
            'short_url' : str(url['_id']),
            'clicks' : url.get('clicks', 0),
            'long_url' : url['long_url']
        })
    return all_urls_data