from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import DECIMAL, Column, ForeignKey, String, INTEGER, TIMESTAMP
from model.places import Places

Base = declarative_base()


class Events(Base):
    __tablename__ = "events"

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    place = Column(INTEGER, ForeignKey(Places.id))
    event_name = Column(String)
    event_time = Column(TIMESTAMP)
    event_duration = Column(INTEGER, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
