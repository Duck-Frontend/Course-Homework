import os


def five():
    students = {}
    file_name = input("Введите название файла: ")

    if file_name in os.listdir():
        with open(file_name, "r", encoding="utf-8") as file:
            file = file.read().splitlines()

            for line in file:
                line = line.strip()
                part = line.rsplit(maxsplit=2)

                if len(part) == 3:
                    name = f"{part[0]} {part[1]}"
                    grade = int(part[2])
                    students[name] = grade

                    if grade < 3:
                        print(f"{name}: {grade}")


five()
