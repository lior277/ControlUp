from typing import List, Optional
from pydantic import BaseModel

class AirportAttributes(BaseModel):
    name: str
    city: str
    country: str
    iata: str
    icao: str
    latitude: str
    longitude: str
    altitude: int
    timezone: str

class AirportData(BaseModel):
    id: str
    type: str
    attributes: AirportAttributes

class DistanceAirport(BaseModel):
    id: int
    name: str
    city: str
    country: str
    iata: str
    icao: str
    latitude: str
    longitude: str
    altitude: int
    timezone: str

class DistanceAttributes(BaseModel):
    from_airport: DistanceAirport
    to_airport: DistanceAirport
    kilometers: float
    miles: float
    nautical_miles: float

class DistanceData(BaseModel):
    id: str
    type: str
    attributes: DistanceAttributes

class Links(BaseModel):
    first: str
    self: str
    last: str
    prev: Optional[str] = None
    next: Optional[str] = None

class DistanceResponse(BaseModel):
    data: DistanceData

class AirportResponse(BaseModel):
    data: List[AirportData]
    links: Links