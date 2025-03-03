from pydantic import BaseModel, HttpUrl
from datetime import datetime

class URLSchema(BaseModel):
    """
    Schema for the URL data.

    Attributes:
        long_url (HttpUrl): The long URL to be shortened.
    """
    long_url: HttpUrl