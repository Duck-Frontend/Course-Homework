import os

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session


from dotenv import load_dotenv


class Controller:
    def __init__(self):
        load_dotenv()
        self.engine = create_engine(os.environ.get("DB_URL"))
        self.session = Session(self.engine)

    def select_event_id(self, model):
        name = input("введите название мероприятия: ")
        events = select(model.id).where(model.event_name == name)

        with self.engine.connect() as conn:
            for row in conn.execute(events):
                return row[0]
