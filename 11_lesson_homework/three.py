class Car:
    """Класс машины"""

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start_car(self):
        return "Автомобиль заведён"

    def stop_car(self):
        return "Автомобиль заглушен"

    def set_color(self, color):
        self.color = color
        return self.color

    def set_type(self, type):
        self.type = type
        return type

    def set_year(self, year):
        self.year = year
        return self.year
