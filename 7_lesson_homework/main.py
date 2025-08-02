from functools import reduce
from time import time


def count_runtime(function): # Четвёртое задание

    def wrapper(*args, **kwargs):
        count_variable = len(args)
        start = time()
        result = function(*args, **kwargs)
        end = time()

        print(f"Функция {function.__name__} выполнилась за {end - start:.4} с")
        print(f"Функция {function.__name__} содержит {count_variable} переменных")
        return result
    return wrapper


@count_runtime
def one(arr):
    return list(map(lambda string: str(string), arr))


@count_runtime
def two(arr):
    return list(filter(lambda number: False if number > 0 else True, arr))


@count_runtime
def three(arr):
    return list(filter(lambda string: string == string[::-1], arr))


@count_runtime
def five(arr):
    return sum(list(map(lambda x: x["length"] * x["width"], arr)))
