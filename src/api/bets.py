from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from src.schemas.bets import \
    CreateBetRequest, CreateBetResponse, GetBetsResponse
from src.schemas.events import UpdateEventRequest
from src.controllers.manager import ServiceManager, get_service_manager
from src.exceptions import \
    EventNotFoundError, InvalidBetSumError, InvalidEventStatusError


router = APIRouter(prefix="/v1/bets", tags=["Bets"])


@router.post("/bet")
async def create_bet(
    request: CreateBetRequest,
    manager: Annotated[ServiceManager, Depends(get_service_manager)]
) -> CreateBetResponse:
    try:
        event = await manager.line_provider.get_event(request.id_event)
    except EventNotFoundError as ex:
        raise HTTPException(status_code=404, detail=ex)
    try:
        id_bet = await manager.bet_maker.add_bet(event, request)
    except (InvalidBetSumError, InvalidEventStatusError) as ex:
        raise HTTPException(status_code=400, detail=ex)

    return CreateBetResponse(id_bet=id_bet, status="complited")


@router.post("/bets")
async def get_bets(
    manager: Annotated[ServiceManager, Depends(get_service_manager)]
) -> GetBetsResponse:
    return manager.bet_maker.get_bets()


@router.put("/update_bet")
async def update_bet(
    request: UpdateEventRequest,
    manager: Annotated[ServiceManager, Depends(get_service_manager)]
) -> None:
    await manager.bet_maker.update_bets(request)
