from pydantic import BaseModel, HttpUrl
from datetime import datetime

class URLSchema(BaseModel):
    long_url: HttpUrl