import requests
import os
import pandas as pd
from typing import List
from dotenv import load_dotenv

# Load environment variables once, outside of the class
load_dotenv() 

OPENAQ_API_KEY = os.getenv("OPEN_API_KEY")

def get_measurement_by_location(country_code:List)->pd.DataFrame:
    """Get available measurement from the country code for that
        country from the OpenAQ API.
        Should update if the data in openAQ changes.

    Args:
        country_code (List[][]): List of country codes.
        
    Returns:
        pd.DataFrame: Returns a dataframe with measurement.
    """
    
    
    get_measurement_url = "https://api.openaq.org/v2/locations?"

    # Create headers with the API key
    headers = {
        "Api-Key": OPENAQ_API_KEY
    }

    # Create the query string
    query_string = {
        "country": country_code,
        "limit": 10000
    }

    # Make the GET request with the headers
    response = requests.get(get_measurement_url, headers=headers, params=query_string)

    measurement_data = response.json()

    measurement_df = pd.DataFrame(measurement_data["results"])
  
    return measurement_df