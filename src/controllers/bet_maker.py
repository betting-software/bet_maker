import time

from src.db.dao import BetsDAO

from src.schemas.events import Event, Status, UpdateEventRequest
from src.schemas.bets import CreateBetRequest, GetBetsResponse, Bet
from src.exceptions import InvalidBetSumError, InvalidEventStatusError


class BetMakerController:
    def __init__(self):
        self._dao = BetsDAO

    async def add_bet(self, event: Event, request: CreateBetRequest) -> int:
        if event.status != Status.PENDING or event.timestamp < int(time.time()):
            raise InvalidEventStatusError
        if request.bet_sum <= 0:
            raise InvalidBetSumError

        return await self._dao.add_one(
                id_event=event.id, bet_sum=request.bet_sum,
                coefficient=event.coefficient, status=event.status
            )

    async def get_bets(self) -> GetBetsResponse:
        records = await self._dao.select_filter()
        data = [
            Bet(id_bet=record.id, status=record.status.value)
            for record in records
        ]
        return GetBetsResponse(bets=data)

    async def update_bets(self, request: UpdateEventRequest) -> None:
        await self._dao.update_filter(
            update_values={"status": request.status}, id_event=request.id
        )
