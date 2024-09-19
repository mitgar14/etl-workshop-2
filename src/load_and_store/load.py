from database.db_operations import creating_engine, load_clean_data, disposing_engine

import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")

def loading_merged_data(df: pd.DataFrame, table_name: str) -> None:
    """
    Load the clean data to a database.   

    """
    
    logging.info("Loading clean data to the database.")
    
    engine = creating_engine()
    
    try:
        
        df = load_clean_data(engine, df, table_name)
        logging.info("Data loaded to the database.")
        
    except Exception as e:
        logging.error(f"Error loading clean data to the database: {e}.")
    finally:
        disposing_engine(engine)