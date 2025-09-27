import tabulate

from core.view.view import View
from models import Places, Events, Tickers


class CLI:

    def __init__(self):
        self.view = View()

    def show_menu(self):
        self.view.menu()


if __name__ == "__main__":
    app = CLI()
    app.show_menu()
