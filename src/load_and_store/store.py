from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

from dotenv import load_dotenv
import os


import pandas as pd

import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")

load_dotenv("./env/.env")

credentials_file = rf"{os.getenv('DRIVE_CREDENTIALS')}"

# Function to authenticate Google Drive using PyDrive2.
def auth_drive():
    try:
        logging.info("Starting Google Drive authentication process.")
        
        gauth = GoogleAuth()
        gauth.LoadClientConfigFile(credentials_file)
        
        gauth.LocalWebserverAuth()
        logging.info("Local webserver authentication completed successfully.")
                
        drive = GoogleDrive(gauth)
        logging.info("Google Drive authentication completed successfully.")
        
        return drive
    except Exception as e:
        logging.error(f"Authentication error: {e}", exc_info=True)

# Function to upload a merged DataFrame to Google Drive as a CSV file.
def store_merged_data(title, df, folder_id): 
    drive = auth_drive()
    
    logging.info(f"Storing {title} on Google Drive.")
    
    csv_file = df.to_csv(index=False) 
    
    # Create a new file on Google Drive with the specified title and folder.
    file = drive.CreateFile({"title": title,
                             "parents": [{"kind": "drive#fileLink",
                                          "id": folder_id}],
                             "mimeType": "text/csv" })
    
    # Set the content of the file to the CSV data.
    file.SetContentString(csv_file)
    
    file.Upload()
    
    logging.info(f"File {title} uploaded successfully.")