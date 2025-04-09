import pytest
from infrastructure.infra.dal.data_reposetory.data_rep import DataRep
from infrastructure.objects.objects_api.airport_gap import AirportsGap

@pytest.mark.asyncio
async def test_verify_airports_count():
    airports_gap = AirportsGap()
    airports_gap_url = f"{DataRep.airport_gap_uri}airports"

    airports_data = await airports_gap.get_airports_data_async(airports_gap_url)

    assert len(airports_data.data) == 30, \
        f"Expected number of airports: 30, Actual number of airports: {len(airports_data.data)}"
