import aiohttp
from typing import Optional


class ApiAccess:
    def __init__(self):
        self._session: Optional[aiohttp.ClientSession] = None

    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
        return self._session

    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()

    async def execute_get_request_async(self, url: str, headers=None) -> dict:
        session = await self._get_session()
        async with session.get(url, headers=headers) as response:
            if response.status != 200:
                raise Exception(f"Error: Received status code {response.status} for GET request to {url}")
            return await response.json()

    async def execute_post_request_async(self, url: str, data, headers=None) -> dict:
        session = await self._get_session()

        async with session.post(url, data=data, headers=headers) as response:
            if response.status != 200:
                raise Exception(f"Error: Received status code {response.status} for POST request to {url}")
            return await response.json()
