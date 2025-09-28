import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


from dotenv import load_dotenv


class Controller:
    def __init__(self):
        load_dotenv()
        self.engine = create_engine(os.environ.get("DB_URL"))
        self.session = Session(self.engine)
