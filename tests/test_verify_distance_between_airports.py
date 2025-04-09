import pytest
from infrastructure.infra.dal.data_reposetory.data_rep import DataRep
from infrastructure.objects.objects_api.airport_gap import AirportsGap


@pytest.mark.asyncio
async def test_verify_distance_between_airports():
    airports_gap = AirportsGap()

    airports_gap_url = f"{DataRep.airport_gap_uri}airports/distance"
    distance = await airports_gap.get_distance_between_airports(airports_gap_url, "KIX", "NRT")

    assert distance > 400, "Distance should be greater than 400"