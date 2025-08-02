import json
import csv
import re
import os


def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def json_to_csv():
    json_file = input("Введите имя JSON файла: ")
    if not os.path.exists(json_file):
        print("Файл не найден!")
        return
    
    csv_file = input("Введите имя CSV файла для сохранения: ")
    data = load_json(json_file)
    
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data[0].keys())
        for row in data:
            writer.writerow(row.values())
    print(f"Данные сохранены в {csv_file}")

def add_employee_json():
    filename = input("Введите имя JSON файла: ")
    if not os.path.exists(filename):
        print("Файл не найден!")
        return
    
    data = load_json(filename)
    employee = {
        "name": input("Имя: "),
        "birth_year": int(input("Год рождения: ")),
        "height": float(input("Рост: ")),
        "languages": input("Языки программирования (через запятую): ").split(',')
    }
    data.append(employee)
    save_json(data, filename)
    print("Сотрудник добавлен")

def add_employee_csv():
    json_file = input("Введите имя JSON файла: ")
    if not os.path.exists(json_file):
        print("Файл не найден!")
        return
    
    add_employee_json()
    json_to_csv()

def find_by_name():
    filename = input("Введите имя JSON файла: ")
    if not os.path.exists(filename):
        print("Файл не найден!")
        return
    
    name = input("Введите имя для поиска: ")
    data = load_json(filename)
    for emp in data:
        if emp['name'].lower() == name.lower():
            print(emp)
            return
    print("Сотрудник не найден")

def filter_by_language():
    filename = input("Введите имя JSON файла: ")
    if not os.path.exists(filename):
        print("Файл не найден!")
        return
    
    language = input("Введите язык программирования: ")
    data = load_json(filename)
    found = [emp for emp in data if language.lower() in [lang.lower() for lang in emp['languages']]]
    for emp in found:
        print(emp)

def filter_by_year():
    filename = input("Введите имя JSON файла: ")
    if not os.path.exists(filename):
        print("Файл не найден!")
        return
    
    year = int(input("Введите год рождения: "))
    data = load_json(filename)
    heights = [emp['height'] for emp in data if emp['birth_year'] < year]
    if heights:
        print(f"Средний рост: {sum(heights)/len(heights):.2f}")
    else:
        print("Нет сотрудников")

def menu():
    while True:
        print("\n1. Конвертировать JSON в CSV")
        print("2. Добавить сотрудника (JSON)")
        print("3. Добавить сотрудника (CSV)")
        print("4. Найти по имени")
        print("5. Фильтр по языку")
        print("6. Фильтр по году")
        print("7. Выход")
        
        choice = input("Выберите действие: ")
        
        match choice:
            case '1':
                json_to_csv()
            case '2':
                add_employee_json()
            case '3':
                add_employee_csv()
            case '4':
                find_by_name()
            case '5':
                filter_by_language()
            case '6':
                filter_by_year()
            case '7':
                break
            case _:
                print("Неверный ввод")

menu()
