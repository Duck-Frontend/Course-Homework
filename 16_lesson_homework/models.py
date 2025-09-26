from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DECIMAL, Column, ForeignKey, String, INTEGER, TIMESTAMP
from sqlalchemy import Enum

Base = declarative_base()


class Places(Base):
    __tablename__ = "places"
    id = Column(INTEGER, primary_key=True)
    place_name = Column(String(128), nullable=False)
    max_visitors = Column(INTEGER)


class Events(Base):
    __tablename__ = "events"

    id = Column(INTEGER, primary_key=True)
    place = Column(INTEGER, ForeignKey(Places.id))
    event_name = Column(String)
    event_time = Column(TIMESTAMP)
    event_duration = Column(INTEGER, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)


class Tickers(Base):
    __tablename__ = "tickets"
    id = Column(INTEGER, primary_key=True)
    event = Column(INTEGER, ForeignKey(Events.id, ondelete='CASCADE'))
    ticket_status = Column(
        Enum('available', 'booked', 'sold', 'cancelled',
             name='ticket_status_enum'),
        nullable=False,
        default='available'
    )
    created_at = Column(TIMESTAMP)
