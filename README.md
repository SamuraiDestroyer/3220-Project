# 3220-Project
This is Team 3 3220 Project



How to run: testAPIClass

1) First, download testAPIClass.py, TestConfigInNamespace.xml, and SampleCSVFile_556kb.csv to your computer.
2) Open testAPIClass.py in an IDE, then copy and paste the file locations of TestConfigInNamespace.xml and
   SampleCSVFile_556kb.csv into their respective places inside the api_keys_ti_files dictionary.
3) In your terminal, enter: pip install "fastapi[all]". 
4) To run the application, enter into the terminal: uvicorn testAPIClass:app
5) Copy the link that is displayed in the terminal and paste it into your browser to open the temporary webpage.
6) Then, append /api/csvtest or /api/xmltest to the URL in your browser and hit enter.
For example, http://127.0.0.1:8000/api/csvtest will re-download the CSV: SampleCSVFile_556kb.csv
This serves as an example of how developers can connect to our API.
