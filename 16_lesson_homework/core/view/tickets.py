from core.controller.events import Events_Controller
from core.view.view import View
from core.controller.tickets import Tickets_Controller
from core.model.events import Events


class Tickets_View(View):
    def __init__(self):
        self.tickets_controller = Tickets_Controller()
        self.events_controller = Events_Controller()
        self.events_model = Events()

    def reserve_ticket(self):
        id = self.tickets_controller.select_event_id(self.events_model)
        self.tickets_controller.update_ticket_by_name(id, "book")

    def cancel_ticket(self):
        id = self.tickets_controller.select_event_id(self.events_model)
        self.tickets_controller.update_ticket_by_name(id, "cancel")

    def show_tickets(self):
        pass
