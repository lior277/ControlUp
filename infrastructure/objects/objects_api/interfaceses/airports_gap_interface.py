from abc import abstractmethod, ABC

from infrastructure.objects.data_classes.airport import AirportResponse

class IAirportsClient(ABC):
    @abstractmethod
    async def get_airports_data_async(self, url: str) -> AirportResponse:
        pass

    @abstractmethod
    async def get_distance_between_airports(self, url: str, from_code: str, to_code: str) -> float:
        pass