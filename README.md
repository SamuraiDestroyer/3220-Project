# 3220-Project
This is Team 3 3220 Project



How to run: opendataAPIClass

1) First, download the website zip folder to your computer and opendataAPIClass.py.
2) Open opendataAPIClass.py in an IDE, then copy and paste the file locations of the of all the datasets (under comp3220_project/assets/datasets/) into their respective places inside the api_keys_to_files dictionary.
3) In your terminal, enter: pip install "fastapi[all]". 
4) To run the application, enter into the terminal: uvicorn opendataAPIClass:app
5) Copy the link that is displayed in the terminal and paste it into your browser to open the temporary webpage.
6) Then, append /api/ (the dataset api key) / (and its type) / to the URL in your browser and hit enter.
For example, http://127.0.0.1:8000/api/Internationalinvestmentposition/csv will re-download the CSV: International_IP.csv
This serves as an example of how developers can connect to our API.
