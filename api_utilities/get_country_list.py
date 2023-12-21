import os
import requests
import pandas as pd
from typing import List
from dotenv import load_dotenv



load_dotenv()  # Load environment variables once, outside of the class
OPENAQ_API_KEY = os.getenv("OPEN_API_KEY")

def country_list()->List:
    """Get a list of available countries from the OpenAQ API.
        Should update if the data in openAQ changes.
    """
    get_countries_url = "https://api.openaq.org/v2/countries"
    
    # Create headers with the API key
    headers = {
        "Api-Key": OPENAQ_API_KEY
    }

    # Make the GET request with the headers
    response = requests.get(get_countries_url, headers=headers)

    country_data = response.json()


    country_df =  pd.DataFrame(country_data["results"])
    country_df = country_df[["code", "name"]]
    return country_df.values.tolist()
