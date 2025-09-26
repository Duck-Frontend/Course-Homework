from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, JSON, INTEGER


Base = declarative_base()


class Events(Base):
    __tablename__ = "events"

    id = Column(INTEGER, primary_key=True)
    enroll = Column(INTEGER)
    personal_info = Column(JSON)
    name = Column(String(255))


class Places(Base):
    __tablename__ = "places"

    id = Column(INTEGER, primary_key=True)
    place_name = Column(String(128), nullable=False)
