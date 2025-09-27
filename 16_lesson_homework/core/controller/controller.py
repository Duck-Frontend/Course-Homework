import os

from models import Places, Events, Tickers

from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import Session

from datetime import datetime

from dotenv import load_dotenv


class Controller:
    def __init__(self):
        load_dotenv()
        self.engine = create_engine(os.environ.get("DB_URL"))
        self.session = Session(self.engine)

    def select_all_events(self):
        events = select(
            Places.place_name.label('place_name'),
            Events.event_name.label('event_name'),
            Events.event_time,
            Events.event_duration,
            Events.price
        ).join(
            Places, Events.place == Places.id  # JOIN по внешнему ключу
        )

        data = [['Название места', 'Название мероприятия',
                 'Время начала', 'Длительность', 'Цена билета']]

        with self.engine.connect() as conn:
            for row in conn.execute(events):
                data.append(list(row))

        return data

    def select_event_by_name(self):
        name = input("Введите название мероприятия: ")
        events = select(
            Places.place_name.label("place_name"),
            Events.event_name.label('event_name'),
            Events.event_time,
            Events.event_duration,
            Events.price
        ).join(
            Places, Events.place == Places.id  # JOIN по внешнему ключу
        ).where(Events.event_name == name)

        data = [['Название места', 'Название мероприятия',
                 'Время начала', 'Длительность', 'Цена билета']]

        with self.engine.connect() as conn:
            for row in conn.execute(events):
                data.append(list(row))

        return data

    def select_event_by_place(self):
        name = input("Введите название места: ")
        events = select(
            Places.place_name.label("place_name"),
            Events.event_name.label('event_name'),
            Events.event_time,
            Events.event_duration,
            Events.price
        ).join(
            Places, Events.place == Places.id  # JOIN по внешнему ключу
        ).where(Places.place_name == name)

        data = [['Название места', 'Название мероприятия',
                 'Время начала', 'Длительность', 'Цена билета']]

        with self.engine.connect() as conn:
            for row in conn.execute(events):
                data.append(list(row))

        return data

    def select_event_id(self):
        name = input("Введите название мероприятия: ")
        events = select(Events.id).where(Events.event_name == name)

        with self.engine.connect() as conn:
            for row in conn.execute(events):
                return row[0]

    def update_ticket_by_name(self, id, method):
        if method == "cancel":
            try:
                self.session.query(Tickers).filter(
                    Tickers.event == id).update({'ticket_status': "cancelled"})
                print("Succses")
            except:
                pass
        elif method == "book":
            try:
                self.session.query(Tickers).filter(
                    Tickers.event == id).update({'ticket_status': 'booked'})
                print("Succses")
            except:
                pass

    def create_event(self):
        # Сбрасываем последовательность ID
        self.session.execute(
            text("SELECT setval('events_id_seq', (SELECT MAX(id) FROM events))"))
        self.session.commit()

        place_id = int(input("Введите ID места: "))
        event_name = input("Введите название мероприятия: ")
        event_time = input("Введите время (гггг-мм-дд чч:мм:сс): ")
        event_duration = int(input("Введите продолжительность (мин): "))
        price = float(input("Введите цену билета: "))

        new_event = Events(
            place=place_id,
            event_name=event_name,
            event_time=datetime.strptime(event_time, '%Y-%m-%d %H:%M:%S'),
            event_duration=event_duration,
            price=price
        )

        self.session.add(new_event)
        self.session.commit()

        print(f"Мероприятие '{event_name}' создано! ID: {new_event.id}")
