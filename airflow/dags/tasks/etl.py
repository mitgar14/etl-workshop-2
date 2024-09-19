# Importing the necessary modules
# --------------------------------

from extract.spotify_extract import extracting_spotify_data
from extract.grammys_extract import extracting_grammys_data

import json
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


# Creating tasks functions
# ------------------------

def extract_spotify():
    try:
        df = extracting_spotify_data("./data/spotify_dataset.csv") 
        return df.to_json(orient="records")
    except Exception as e:
        logging.error(f"Error extracting data: {e}")

def extract_grammys():
    try:
        df = extracting_grammys_data()
        return df.to_json(orient="records")
    except Exception as e:
        logging.error(f"Error extracting data: {e}")