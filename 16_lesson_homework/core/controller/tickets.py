from core.controller.controller import Controller
from core.model.tickets import Tickets


class Tickets_Controller(Controller):

    def show_tickets_by_event(self, event_id):
        pass

    def update_ticket_by_name(self, id, method):
        if method == "cancel":
            try:
                self.session.query(Tickets).filter(
                    Tickets.event == id).update({'ticket_status': "cancelled"})
                print("Succses")
            except:
                pass
        elif method == "book":
            try:
                self.session.query(Tickets).filter(
                    Tickets.event == id).update({'ticket_status': 'booked'})
                print("Succses")
            except:
                pass
