from core.model.events import Events
from core.model.events import Places

from core.controller.controller import Controller

from sqlalchemy import select, text
from datetime import datetime


class Events_Controller(Controller):

    def select_all_events(self):
        events = select(
            Places.place_name.label('place_name'),
            Events.event_name.label('event_name'),
            Events.event_time,
            Events.event_duration,
            Events.price
        ).join(
            Places, Events.place == Places.id
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
            Places, Events.place == Places.id
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
            Places, Events.place == Places.id
        ).where(Places.place_name == name)

        data = [['Название места', 'Название мероприятия',
                 'Время начала', 'Длительность', 'Цена билета']]

        with self.engine.connect() as conn:
            for row in conn.execute(events):
                data.append(list(row))

        return data

    def create_event(self):
        # Не знаю почему не работает autoincrement но без этого костыля выкидывает ошибку существующего id
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
