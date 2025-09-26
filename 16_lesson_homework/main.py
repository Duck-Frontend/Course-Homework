import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class UI:

    def cli(self):
        pass


def main():
    load_dotenv()

    engine = create_engine(os.environ.get("DB_URL"))
    engine.connect()

    session = Session(engine)


if __name__ == "__main__":
    main()
