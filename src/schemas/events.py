from enum import Enum

from pydantic import BaseModel


class Status(Enum):
    PENDING = "pending"
    TEAM_1_WINS = "team_1_wins"
    TEAM_2_WINS = "team_2_wins"


class UpdateEventRequest(BaseModel):
    id: int
    status: Status


class BaseEvent(BaseModel):
    name: str
    coefficient: float
    timestamp: int
    status: Status


class Event(BaseEvent):
    id: int


class EventsResponse(BaseModel):
    events: list[Event]