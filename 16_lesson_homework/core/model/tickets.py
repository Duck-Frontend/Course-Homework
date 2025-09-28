from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, ForeignKey, INTEGER, TIMESTAMP
from sqlalchemy import Enum

from core.model.events import Events

Base = declarative_base()


class Tickets(Base):
    __tablename__ = "tickets"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    event = Column(INTEGER, ForeignKey(Events.id, ondelete='CASCADE'))
    ticket_status = Column(
        Enum('available', 'booked', 'sold', 'cancelled',
             name='ticket_status_enum'),
        nullable=False,
        default='available'
    )
    created_at = Column(TIMESTAMP)
