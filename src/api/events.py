from typing import Annotated

from fastapi import APIRouter, Depends

from src.schemas import events
from src.controllers.manager import ServiceManager, get_service_manager


router = APIRouter(prefix="/v1/events", tags=["Events"])


@router.get("/events")
async def get_events(
    manager: Annotated[ServiceManager, Depends(get_service_manager)]
) -> events.EventsResponse:
    return await manager.line_provider.get_events()
