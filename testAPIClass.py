from fastapi import FastAPI

from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException, Path

app = FastAPI()
api_keys_to_files = {
    "csvtest": 'SampleCSVFile_556kb.csv',
    "xmltest": 'TestConfigInNamespace.xml',
    # Add more keys and file paths as needed
}


@app.get('/')
async def root():
    return {'Webpage'}

@app.get('/api/csv/test')
async def download_csv():
    file_path = r'C:\Users\16479\PycharmProjects\COMP-3220\SampleCSVFile_556kb.csv'  # Update this to the actual path of your CSV file
    return FileResponse(path=file_path, filename="SampleCSVFile_556kb.csv", media_type='text/csv')

@app.get('/api/xml/test')
async def download_csv():
    file_path = r'C:\Users\16479\PycharmProjects\COMP-3220\TestConfigInNamespace.xml'  # Update this to the actual path of your CSV file
    return FileResponse(path=file_path, filename="TestConfigInNamespace.xml", media_type='application/xml')

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
