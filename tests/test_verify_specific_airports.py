import pytest
from infrastructure.infra.dal.data_reposetory.data_rep import DataRep
from infrastructure.objects.objects_api.airport_gap import AirportsGap

@pytest.mark.asyncio
async def test_verify_specific_airports():
    expected_airports = [
        "Akureyri Airport",
        "St. Anthony Airport",
        "CFB Bagotville"
    ]

    airports_gap = AirportsGap()
    airports_gap_url = f"{DataRep.airport_gap_uri}airports"

    airports_data = await airports_gap.get_airports_data_async(airports_gap_url)
    actual_airport_names = [airport.attributes.name for airport in airports_data.data]

    for expected_airport in expected_airports:
        assert expected_airport in actual_airport_names, f"Airport '{expected_airport}' was not found in the response"