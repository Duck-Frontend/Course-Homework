import re


def two():
    with open("./text.txt", "r+") as text:
        text = text.read()

        reg = r'\b[А-ЯЁ][а-яё]*-?[А-ЯЁ]?[а-яё]* [А-ЯЁ][а-яё]* [А-ЯЁ][а-яё]*\b'
        return re.sub(reg, "N", text)


print(two())
