import os
import tabulate

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from simple_term_menu import TerminalMenu


class CLI:

    def __init__(self):
        load_dotenv()

        self.engine = create_engine(os.environ.get("DB_URL"))
        self.session = Session(self.engine)
        self.__menu_items = [
            "Просмотр мероприятий",
            "Добавить мероприятие",
            "Поиск мероприятия по названию",
            "Поиск мероприятия по месту",
            "Забронировать билет",
            "Отменить бронь",
            "Выход"]

    def menu(self):
        menu = TerminalMenu(self.__menu_items)
        user_chose = menu.show()

        match user_chose:
            case 0: self.__show_all_events()
            case 1: self.__add_event()
            case 2: self.__find_event_by_name()
            case 3: self.__find_events_by_place()
            case 4: self.__reserve_ticket()
            case 5: self.__cancel_ticket()
            case 6: exit()

    # CRUD
    def __show_all_events(self):

        result = self.session.execute(text("SELECT * FROM events"))
        results = tabulate.tabulate(result.all())

        print(results)
        return self

    def __add_place(self):
        event_name = input("Введите название мероприятия: ")
        event_price
        event_time

    def __add_event(self):
        pass

    def __edit_event(self):
        pass

    def __delete_event(self):
        pass

    def __find_event_by_name(self):
        pass

    def __find_events_by_place(self):
        pass

    def __searh_events_partial(self):
        pass

    def __reserve_ticket(self):
        pass

    def __cancel_ticket(self):
        pass

    def __show_tickets(self):
        pass


if __name__ == "__main__":
    app = CLI()
    app.menu()
