
from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException

app = FastAPI()
api_keys_to_files = {
    "csvtest": r'SampleCSVFile_556kb.csv file path here',
    "xmltest": r'TestConfigInNamespace.xml file path here',
    # Add more keys and file paths as needed
}


@app.get('/')
async def root():
    return {'Webpage'}

@app.get('/api/{api_key}')
async def download_csv(api_key: str):

    if api_key in api_keys_to_files:
        file_path = api_keys_to_files[api_key]
        filename = file_path.split('\\')[-1]

        if file_path.lower().endswith('.csv'):
            media_type = 'text/csv'
        elif file_path.lower().endswith('.xml'):
            media_type = 'application/xml'
        else:
            raise HTTPException(status_code=404, detail="Type not supported.")

        return FileResponse(path=file_path, filename=filename, media_type=media_type)
    raise HTTPException(status_code=404, detail="File not found for the provided API key.")
