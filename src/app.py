from fastapi import FastAPI

from src.api.events import router as events_router
from src.api.bets import router as bets_router


app = FastAPI(
    title="BET MAKER API",
    description="API for work with bets and events",
    version="1.0.0",
)


app.include_router(events_router)
app.include_router(bets_router)
