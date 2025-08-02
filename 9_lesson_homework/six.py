import os
import re


def six():

    file_name = input("Введите название файла: ")

    if file_name in os.listdir():
        with open(file_name, "r", encoding="utf-8") as file:
            file = file.read()

            numbers = re.findall(r'\d+', file)
            numbers = [int(num) for num in numbers]

            total = sum(numbers)

            print(f"Сумма всех чисел в файле: {total}")
    else:
        print("Нет такого файла!")


six()
