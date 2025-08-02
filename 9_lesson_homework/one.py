import os
import re


def one():
    print(os.name)
    print(os.getcwd())

    files_in_directory = os.listdir()
    files_count = 0
    files_size = 0

    for file in files_in_directory:
        files_count += 1
        files_size += os.path.getsize(file)

        if not os.path.isfile(file):  # Пропуск директорий
            continue

        extension = re.search(r"(?<=\.)[^./\\]+$", file)

        if not extension:
            continue  # Пропускаем файлы без расширений

        extension = extension.group().lower()
        target_folder = extension

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        try:
            os.replace(file, os.path.join(target_folder, file))
        except FileExistsError:
            print(f"Файл {file} уже существует в папке {target_folder}!")

    print(f"Количество файлов: {files_count}")
    # В формуле совершенно не уверен
    print(f"Общий размер всех файлов {files_size / (1024 ** 2)} МБ")


one()
