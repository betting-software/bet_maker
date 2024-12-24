from pydantic import BaseModel

from src.schemas.events import Status


class CreateBetRequest(BaseModel):
    id_event: int
    bet_sum: float


class CreateBetResponse(BaseModel):
    id_bet: int
    status: str


class Bet(BaseModel):
    id_bet: int
    status: Status


class GetBetsResponse(BaseModel):
    bets: list[Bet]
