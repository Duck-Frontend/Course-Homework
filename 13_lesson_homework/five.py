class Calculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        return self.strategy.execute(a, b)


class Addition:
    def execute(self, a, b):
        return a + b


class Subtraction:
    def execute(self, a, b):
        return a - b


class Multiplication:
    def execute(self, a, b):
        return a * b


class Division:
    def execute(self, a, b):
        return a / b
