import aiohttp

from src.config import line_provider_config
from src.schemas.events import Event, EventsResponse
from src.exceptions import EventNotFoundError


class LineProviderController:
    def __init__(self):
        self._line_provider_url = line_provider_config.line_provider_url

    async def get_event(self, id_event) -> Event | None:
        url = f"{self._line_provider_url}/v1/events/event/{id_event}"
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            if response.status == 200:
                data = await response.json()
                return Event(**data)
            raise EventNotFoundError

    async def get_events(self) -> EventsResponse:
        url = f"{self._line_provider_url}/v1/events/events"
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            if response.status == 200:
                data = await response.json()
                return EventsResponse(**data)
            raise EventNotFoundError
