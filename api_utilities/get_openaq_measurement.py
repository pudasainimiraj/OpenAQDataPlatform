import requests
import os
import pandas as pd
from datetime import datetime
from ratelimit import limits, sleep_and_retry
from typing import List
from dotenv import load_dotenv

# Load environment variables once, outside of the class
load_dotenv()

OPENAQ_API_KEY = os.getenv("OPENAQ_API_KEY")

@sleep_and_retry
@limits(calls=1, period=1)
def get_all_measurement_by_country(country_code:List)->pd.DataFrame:
    """Get available measurement from the country code for that
        country from the OpenAQ API.
        Should update if the data in openAQ changes.

    Args:
        country_code (List[][]): List of country codes.

    Returns:
        pd.DataFrame: Returns a dataframe with measurement.
    """

    get_measurement_url = "https://api.openaq.org/v2/measurements?"


    # Create headers with the API key
    headers = {
        "Api-Key": OPENAQ_API_KEY
    }

    # Create the query string
    query_string = {
        "date_from":"2015-01-01",
        "date_to":str(datetime.now().strftime("%Y-%m-%d")),
        "limit": 3000,
        "page": 1,
        "offset": 0,
        "sort": "desc",
        "radius": 1000,
        "country": country_code,
        "order_by": "datetime"
    }

    # Make the GET request with the headers
    response = requests.get(get_measurement_url, headers=headers, params=query_string)

    if response.status_code == 200:
        measurement_data = response.json()
        measurement_df = pd.DataFrame(measurement_data["results"])
        return measurement_df
    else:
        # Handle error or unsuccessful response
        print(f"Error: {response.status_code}")
        return pd.DataFrame()