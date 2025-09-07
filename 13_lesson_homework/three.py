class Pizza:
    """Класс пицца"""

    def __init__(self,
                 size="", cheese="",
                 pepperoni="", mushrooms="",
                 onions="", bacon=""):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon


class PizzaBuilder:
    """Паттерн Строитель"""

    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def set_cheese(self, cheese):
        self.pizza.cheese = cheese
        return self

    def set_pepperoni(self, pepperoni):
        self.pizza.pepperoni = pepperoni
        return self

    def set_mushrooms(self, mushrooms):
        self.pizza.mushrooms = mushrooms
        return self

    def set_onions(self, onions):
        self.pizza.onions = onions
        return self

    def set_bacon(self, bacon):
        self.pizza.bacon = bacon
        return self

    def build(self):
        return self.pizza


class PizzaDirector:

    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self, size,
                   cheese=False, pepperoni=False,
                   mushrooms=False, onions=False, bacon=False):
        self.builder.set_size(size)
        if cheese:
            self.builder.add_cheese()
        if pepperoni:
            self.builder.add_pepperoni()
        return self.builder.build()
