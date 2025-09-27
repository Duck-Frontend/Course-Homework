import os
import tabulate


from core.controller.controller import Controller

from simple_term_menu import TerminalMenu


class View:
    def __init__(self):
        self.controller = Controller()
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
            case 0:
                self.show_all_events(self.controller.select_all_events())
            case 1:
                self.__add_event()
            case 2:
                self.__find_event_by_name(
                    self.controller.select_event_by_name())
            case 3:
                self.__find_events_by_place(
                    self.controller.select_event_by_place())
            case 4:
                self.__reserve_ticket()
            case 5:
                self.__cancel_ticket()
            case 6:
                exit()
        return self

    def show_all_events(self, data):
        print(tabulate.tabulate(data))

        # event_name = input("Введите название мероприятия: ")
        # event_price = float(input())
        # event_time = input()

    def __add_event(self):
        self.controller.create_event()

    def __edit_event(self):
        pass

    def __delete_event(self):
        pass

    def __find_event_by_name(self, data):
        print(tabulate.tabulate(data))

    def __find_events_by_place(self, data):
        print(tabulate.tabulate(data))

    def __searh_events_partial(self):
        pass

    def __reserve_ticket(self):
        id = self.controller.select_event_id()
        self.controller.update_ticket_by_name(id, "book")

    def __cancel_ticket(self):
        id = self.controller.select_event_id()
        self.controller.update_ticket_by_name(id, "cancel")

    def __show_tickets(self):
        pass
