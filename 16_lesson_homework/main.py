from simple_term_menu import TerminalMenu

from core.view.events import Events_View
from core.view.tickets import Tickets_View


class CLI:

    def __init__(self):
        self.view_events = Events_View()
        self.view_tickets = Tickets_View()
        self.__menu_items = [
            "Просмотр мероприятий",
            "Добавить мероприятие",
            "Поиск мероприятия по названию",
            "Поиск мероприятия по месту",
            "Забронировать билет",
            "Отменить бронь",
            "Выход"]

    def show_menu(self):
        menu = TerminalMenu(self.__menu_items)
        user_chose = menu.show()

        match user_chose:
            case 0:
                self.view_events.show_all_events()
            case 1:
                self.view_events.add_event()
            case 2:
                self.view_events.find_event_by_name()
            case 3:
                self.view_events.find_events_by_place()
            case 4:
                self.view_tickets.reserve_ticket()
            case 5:
                self.view_tickets.cancel_ticket()
            case 6:
                exit()
        return self


if __name__ == "__main__":
    app = CLI()
    app.show_menu()
