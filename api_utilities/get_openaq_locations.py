import requests
import os
import pandas as pd
from ratelimit import limits, sleep_and_retry
from typing import List
from dotenv import load_dotenv

# Load environment variables once, outside of the class
load_dotenv()

OPENAQ_API_KEY = os.getenv("OPEN_API_KEY")

@sleep_and_retry
@limits(calls=1, period=1)
def get_all_locations(country_code:List)->pd.DataFrame:
    """Get available measurement from the country code for that
        country from the OpenAQ API.
        Should update if the data in openAQ changes.

    Args:
        country_code (List[][]): List of country codes.

    Returns:
        pd.DataFrame: Returns a dataframe with measurement.
    """

    get_measurement_url = "https://api.openaq.org/v2/locationss?"

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

    locations_data = response.json()

    locations_df = pd.DataFrame(locations_data["results"])

    return locations_df