class Soda:
    """Класс определяющий вкус газировки"""

    def __init__(self, taste=None):
        self.taste = taste

    def print_taste(self):

        if self.taste:
            return f"У вас газировка с <{self.taste}> вкусом"
        else:
            return "У вас обычная газировка"
