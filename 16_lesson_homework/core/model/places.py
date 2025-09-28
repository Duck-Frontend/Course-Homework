from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,  String, INTEGER

Base = declarative_base()


class Places(Base):
    __tablename__ = "places"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    place_name = Column(String(128), nullable=False)
    max_visitors = Column(INTEGER)
