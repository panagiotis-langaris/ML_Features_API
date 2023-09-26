from fastapi import FastAPI, File, UploadFile
import json
import logging
from getFeatures import feature_extraction

''' Configure logging '''
logging.basicConfig(
    filename="app.log",  # Log file name
    level=logging.INFO,  # Log level (INFO, WARNING, ERROR, DEBUG, etc.)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# Create a logger instance
logger = logging.getLogger(__name__)


### API Metadata definition 
description = """
An API for a feature engineering module that generates some features/variables that are useful for modeling. 🚀


## Health Check

You can **check the health** of the API module.

## Get Features

You will be able to:

* **Get a JSON file with the extracted features**.
* **Get descriptions for the new features** (_not implemented_).
"""

tags_metadata = [
    {
        "name": "Health check",
        "description": "Check API health. See if API is **UP**.",
    },
    {
        "name": "Get features",
        "description": "Send the original data set to the module, and receive a file with the extracted features.",
    },
]

# Create instance of the app
app = FastAPI(
    title="Feature Engineering API",
    description=description,
    summary="A feature engineering API module to be used in an ML pipeline.",
    version="0.0.1",
    contact={
        "name": "Panagiotis Langaris",
        "url": "https://panagiotis-langaris.github.io/",
        "email": "panoslaggaris@gmail.com",
    },
    openapi_tags = tags_metadata,
)

''' Checking the health of the API returns only {status: "UP"} if the API is up and running. '''
@app.get("/health_check/", tags=["Health check"])
def health_check():
    logger.info("Health Check endpoint accessed")
    return {"status": "UP"}

''' Uploading the data in a JSON format and returning the results of the 'feature engineering' process in a JSON format '''
@app.post("/get_features", tags=["Get features"])
async def get_features(file: UploadFile = File(...)):
    try:
        json_data = json.load(file.file)
        features_extracted = feature_extraction(json_data)
        logger.info("Get Features endpoint accessed successfully")
        return {"features_extracted": features_extracted}
    except ValueError:
        logger.error(f"Get Features endpoint failed: Bad request")
        return {"error": "Invalid JSON format in the file"}, 400  # Bad request response // uploaded file has an issue
    except Exception as e:
        logger.error(f"Get Features endpoint failed: {str(e)}")
        return {"error": str(e)}, 500  # Internal Server  error for any other exception




#if __name__ == '__main__':
#    import uvicorn
#    uvicorn.run(app, port=8000)