from math import cos, sqrt, pi, sin


def first():
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    x = float(input("Введите число x: "))

    y_a = (a**2 / 3) + ((a**2 + 4) / b) + \
        (sqrt(a**2 + 4) / 4) + (sqrt((a**2 + 4)**3) / 4)
    y_b = cos(x) + sin(x)
    y_c = (cos(x**2)**2 + sin(2*x - 1)**2) ** (1/3)
    y_d = 5*x + 3*x**2 * sqrt(1 + sin(x)**2)

    print("\nРезультаты:")
    print("a) Результат:", y_a)
    print("b) Результат:", y_b)
    print("c) Результат:", y_c)
    print("d) Результат:", y_d)


def second():
    i = float(input("Годовая ставка (%): ")) / 100
    s = float(input("Сумма кредита: "))
    n = int(input("Срок (месяцев): "))

    p = i / 12
    m = (s * p * (1 + p)**n) / ((1 + p)**n - 1)
    total = m * n
    over = total - s

    print("\nИтоги расчёта:")
    print("Платёж в месяц:", m)
    print("Всего выплатите:", total)
    print("Переплата:", over)
    print("Это", over/s*100, "% от суммы кредита")


def third():
    print("Первая планета:")
    r1 = float(input("Радиус орбиты (млн км): ")) * 1000000
    v1 = float(input("Скорость (км/ч): "))

    print("\nВторая планета:")
    r2 = float(input("Радиус орбиты (млн км): ")) * 1000000
    v2 = float(input("Скорость (км/ч): "))

    year1_hours = (2 * r1 * pi) / v1
    year2_hours = (2 * r2 * pi) / v2
    year1_days = year1_hours / 24
    year2_days = year2_hours / 24
    year1_years = year1_days / 365
    year2_years = year2_days / 365

    longer = year1_years > year2_years

    print("\nРезультаты:")
    print("1-я планета:", year1_years, "земных лет (", year1_days, "дней)")
    print("2-я планета:", year2_years, "земных лет (", year2_days, "дней)")
    if longer:
        print("\nГод на первой планете длиннее!")
    else:
        print("\nГод на первой планете короче!")


# Вызов всех функций по очереди
if __name__ == "__main__":
    first()
    second()
    third()
