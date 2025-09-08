def two(finish):
    numbers = [1, 2, 3]
    count = 0
    while count < finish:
        for num in numbers:
            yield num
            count += 1
