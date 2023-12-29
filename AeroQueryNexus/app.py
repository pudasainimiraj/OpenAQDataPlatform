from typing import Union
from fastapi import FastAPI


from OpenAQDataPlatform.app.cqrs.queries import get_all_locations, get_all_measurements_by_locations

app = FastAPI()

@app.get("/v1/locations")
async def get_all_locations():
    locations = get_all_locations()
    
    return locations

@app.get("/v1/measurements/{locations_id}")
async def get_measurements_by_locations(locations_id: str):
    measurements = get_all_measurements_by_locations(locations_id)
    
    return measurements