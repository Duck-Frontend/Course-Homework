import os


def seven():
    shift = 0
    file_name = input("Введите название файла: ")

    if file_name in os.listdir():
        with open(file_name, "r", encoding="utf-8") as file:
            file = file.readlines()

            for line in file:
                shift += 1
                line = line.strip()

                # Разбираем на отдельные символы и смещаем их на размер shift
                line = [ord(char) + shift for char in line]
                line = [chr(char) for char in line]

                print("".join(line))
    else:
        print("Нет такого файла!")


seven()
