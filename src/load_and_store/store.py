from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

from dotenv import load_dotenv
import os

import pandas as pd

import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")

# Cargar las variables de entorno desde .env
load_dotenv("./env/.env")

client_secrets_file = rf"{os.getenv('CLIENT_SECRETS_PATH')}"
settings_file = rf"{os.getenv('SETTINGS_PATH')}"
credentials_file = rf"{os.getenv('CREDENTIALS_FILE_PATH')}"

# Function to authenticate Google Drive using PyDrive2.
def auth_drive():
    try:
        logging.info("Starting Google Drive authentication process.")

        gauth = GoogleAuth(settings_file=settings_file)
        
        if os.path.exists(credentials_file):
            gauth.LoadCredentialsFile(credentials_file)
            if gauth.access_token_expired:
                logging.info("Access token expired, refreshing token.")
                gauth.Refresh()
            else:
                logging.info("Using saved credentials.")
        else:
            logging.info("Saved credentials not found, performing web authentication.")
            
            gauth.LoadClientConfigFile(client_secrets_file)
            gauth.LocalWebserverAuth()
            gauth.SaveCredentialsFile(credentials_file)
            
            logging.info("Local webserver authentication completed and credentials saved successfully.")

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
    
    file = drive.CreateFile({
        "title": title,
        "parents": [{"kind": "drive#fileLink", "id": folder_id}],
        "mimeType": "text/csv"
    })
    
    # Set the content of the file to the CSV data.
    file.SetContentString(csv_file)
    
    file.Upload()
    
    logging.info(f"File {title} uploaded successfully.")