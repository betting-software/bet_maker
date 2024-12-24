from sqlalchemy import Column, Integer, Float, Enum

from src.db.core import Base
from src.config import db_config
from src.schemas.events import Status


class Bets(Base):
    __tablename__ = db_config.db_table_name

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_event = Column(Integer)
    bet_sum = Column(Float)
    coefficient = Column(Float)
    status = Column(Enum(Status))
    profit = Column(Float, default=None)
