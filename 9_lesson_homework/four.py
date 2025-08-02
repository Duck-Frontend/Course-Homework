import os
import re


def four():
    if "stop_words.txt" not in os.listdir():
        print("Нет файла с запрещёнными словами")
        return

    with open("stop_words.txt", "r", encoding="utf-8") as f:
        stop_words = f.read().split()

    file_name = input("Введите название файла: ")

    if file_name not in os.listdir():
        print("Нет такого файла")
        return

    with open(file_name, "r", encoding="utf-8") as f:
        text = f.read()

    pattern = r'(?<!\w)(' + '|'.join(map(re.escape, stop_words)) + r')(?!\w)'
    result = re.sub(pattern, lambda m: '*' * len(m.group()),
                    text, flags=re.IGNORECASE)

    print(result)


four()
