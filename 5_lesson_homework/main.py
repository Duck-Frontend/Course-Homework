# pylint: skip-file
import math


def one():
    x = float(input())
    n = int(input())

    sin_approx = 0

    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        sin_approx += term

    cos_approx = 0

    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
        cos_approx += term

    print(math.sin(x))
    print(math.cos(x))


def two():
    n = int(input())
    k = int(input())
    d = 0
    s = 0

    while s < n:
        d += 1
        if d % 7 != 0:
            s += k
    print(d)


def three():
    r = int(input())
    arr = [1]

    if len(arr) < 2:
        arr.append(1)

    for i in range(1, r):
        arr.append(arr[i - 1] + arr[i])

    return arr


def four():
    arr = [1, 2, 3]
    count = 0
    min = arr[0]
    max = arr[0]

    for i in arr:
        count += i
        if i > max:
            max = i
        if i < min:
            min = i
    print(f"Сумма:{count}")
    print(f"Минимальное значение: {min}")
    print(f"Максимальное значение: {max}")


def five():
    numbers = [2, 2, 3, 4, 5, 6]
    duplicates = []

    for num in numbers:
        if numbers.count(num) > 1 and num not in duplicates:
            duplicates.append(num)

    if not duplicates:
        print("Все элементы уникальны")
    else:
        print("Не все элементы уникальны. Дубликаты:")
        for num in duplicates:
            print(f"{num}: {numbers.count(num)} раз(а)")


def six(arr, search_item):
    min = 0
    max = len(arr) - 1

    while min <= max:

        mid = (min + max) // 2
        guess = arr[mid]

        if search_item == guess:
            return mid
        elif search_item < guess:
            max = mid - 1
        else:
            min = mid + 1

    return None


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def seven(arr, search_item):
    arr = quick_sort(arr)

    min = 0
    max = len(arr) - 1

    while min <= max:

        mid = (min + max) // 2
        guess = arr[mid]

        if search_item == guess:
            return mid
        elif search_item < guess:
            max = mid - 1
        else:
            min = mid + 1

    return None


# print(seven([5, 6, 7, 1, 2, 3, 4], 2))
