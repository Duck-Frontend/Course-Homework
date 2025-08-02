import os


def three():
    count_dict = {}
    word = ""
    max_count = 0

    file_name = input("Введите название файла: ")

    if file_name in os.listdir():
        with open(file_name, "r", encoding="utf-8") as file:
            all_words = file.read().split()
            all_words = [i.lower() for i in all_words if len(i) > 1]

            for word in all_words:
                if word in count_dict:
                    count_dict[word] += 1
                else:
                    count_dict[word] = 1

            for key, value in count_dict.items():
                if value > max_count:
                    word = key
                    max_count = value

        print(f"Самое часто встречаемое слово: {
            word}, оно встечалось: {max_count} раз(а)")


three()
