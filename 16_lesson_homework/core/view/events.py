import tabulate

from core.controller.events import Events_Controller

from core.view.view import View


class Events_View(View):
    def __init__(self):
        self.events_controller = Events_Controller()

    def show_all_events(self):
        data = self.events_controller.select_all_events()
        print(tabulate.tabulate(data))

    def add_event(self):
        self.events_controller.create_event()

    def __edit_event(self):
        pass

    def __delete_event(self):
        pass

    def find_event_by_name(self):
        data = self.events_controller.select_event_by_name()
        print(tabulate.tabulate(data))

    def find_events_by_place(self):
        data = self.events_controller.select_event_by_place()
        print(tabulate.tabulate(data))

    def __searh_events_partial(self):
        pass
