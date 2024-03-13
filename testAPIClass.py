import requests
import json


def aircraft_api_call():
    response = requests.get(
        'https://open.canada.ca/data/dataset/98abeb62-7c76-4dfb-a134-1551f55ede55/resource/1b977865-6f74-4548-b024-d6ca1a6161a3/download/adminaircraft.json')

    return response.json()


def csv_api_call():
    response = requests.get('https://data.novascotia.ca/api/views/w64p-5ue3/rows.csv?accessType=DOWNLOAD')
    return response.json()
