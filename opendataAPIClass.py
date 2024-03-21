
from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException

app = FastAPI()
api_keys_to_files = {
    "Motorizedvehicleregistrations": {
        "csv": r'file path here for download.csv',
        "xml": r'file path here for download.xml',
        "json": r'file path here for download.json'
    },
    "Internationalinvestmentposition": {
        "csv": r'file path here for International_IP.csv'
    },
    "COVID-19testinglocations": {
        "csv": r'file path here for assessment_centre_locations.csv',
        "json": r'file path here for assessment_centre_locations.json'
    },
    "ApprenticeshipAndProvincialLabourForceStatistics": {
        "csv": r'file path here for albertaapprenticeshipandprovinciallabourforcestatistics2007-2012.csv'
    },
    "NationalDefenceProgramInventory": {
        "csv": r'file path here for dnd_pi_dataset-.csv'
    },

    "NaturalGasReservesByMunicipality": {
        "csv": r'file path here for datasets\Natural_gas_reserves_by_municipality.csv',
        "json": r'file path here for Natural_gas_reserves_by_municipality.json',
        "xml": r'file path here for Natural_gas_reserves_by_municipality.xml'
    },
    "NationalParksAndNationalHistoricSites":{
        "csv": r'file path here for nationalParksAndNationalHistoricSites.xml'
    },
    "CPIStatsAndOthers":{
        "csv": r'file path here for 18100256-eng.zip',
        "xml": r'file path here for 18100256-SDMX.zip'
    },
    "NumberOfChildren": {
        "csv": r'file path here for 42100012-eng.zip',
        "xml": r'file path here for 42100012-SDMX.zip'

    }
    # Add more keys and file paths as needed
}


@app.get('/')
async def root():
    return {'Webpage: now'}


@app.get('/api/{filename}/{typeFile}')
async def download_csv(filename: str, typeFile: str):
    if filename in api_keys_to_files and typeFile in api_keys_to_files[filename]:
        file_path = api_keys_to_files[filename][typeFile]
        filename = file_path.split('\\')[-1]

        if file_path.lower().endswith('.csv'):
            media_type = 'text/csv'
        elif file_path.lower().endswith('.xml'):
            media_type = 'application/xml'
        elif file_path.lower().endswith('.json'):
            media_type = 'application/json'
        elif file_path.lower().endswith('.zip'):
            media_type = 'application/zip'
        else:
            raise HTTPException(status_code=404, detail="Type not supported.")

        return FileResponse(path=file_path, filename=filename, media_type=media_type)
    raise HTTPException(status_code=404, detail="File not found for the provided API key.")

