from infrastructure.infra.dal.api_access.api_accsess import ApiAccess
from infrastructure.objects.data_classes.airport import AirportResponse, DistanceResponse
from infrastructure.objects.objects_api.interfaceses.airports_gap_interface import IAirportsClient


class AirportsGap(IAirportsClient):
    def __init__(self) -> None:
        self.__api_access = ApiAccess()

    async def get_airports_data_async(self, url: str) -> AirportResponse:
        response_data = await self.__api_access.execute_get_request_async(url)
        return AirportResponse.model_validate(response_data)

    async def get_distance_between_airports(self, url: str, from_code: str, to_code: str) -> float:
        payload = {
            "from": from_code,
            "to": to_code
        }

        response_data = await self.__api_access.execute_post_request_async(url, payload)
        distance_response = DistanceResponse.model_validate(response_data)
        return distance_response.data.attributes.kilometers