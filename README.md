# URL Shortener Service

This is a URL Shortener Service built with FastAPI. It allows users to shorten long URLs and provides statistics about the shortened URLs.

## Features

- Shorten long URLs
- Redirect to the original long URL using the short URL
- Retrieve statistics about all shortened URLs
- Check the health of the MongoDB connection

## Project Structure

. ├── app │ ├── database.py │ ├── main.py │ ├── routes │ │ ├── shorturl.py │ │ └── statics.py │ └── schema.py └── run.sh

### `app/database.py`

This file handles the connection to the MongoDB database.

### `app/main.py`

This is the main entry point of the FastAPI application. It initializes the application, adds middleware, and includes the routes.

### `app/routes/shorturl.py`

This file contains the routes for shortening URLs and redirecting to the original long URL.

### `app/routes/statics.py`

This file contains the route for retrieving statistics about all shortened URLs.

### `app/schema.py`

This file defines the schema for the URL data using Pydantic.

## Running the Application

To run the application, use the following command:

```bash
./run.sh


This will start the FastAPI application with Uvicorn on port 8001 and load environment variables from local.env.

Endpoints
Home
GET /: Check if the service is running.
URL Shortening
POST /url/shorten: Shorten a given long URL.

Request Body: { "long_url": "http://example.com" }
Response: { "short_url": "short_code", "total_clicks": 0 }
GET /url/{short_code}: Redirect to the original long URL based on the provided short code.

Statistics
GET /statics/urls-data: Retrieve statistics about all shortened URLs.
Response: [ { "short_url": "short_code", "clicks": 0, "long_url": "http://example.com" }, ... ]
Database Health
GET /db-health: Check the health of the MongoDB connection.
Response: { "status": "connected", "message": "MongoDB is connected!" } or { "status": "error", "message": "error_message" }
Environment Variables
The application expects the following environment variable to be set in local.env:

MONGO_URI: The URI for connecting to the MongoDB database.
Dependencies
FastAPI
Uvicorn
Pydantic
httpx
shortuuid
pymongo
Installation
To install the dependencies, run:
pip install -r requirements.txt


