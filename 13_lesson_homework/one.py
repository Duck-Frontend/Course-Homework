def one(finish):
    numbers = []

    for i in range(finish):
        if len(numbers) < 2:
            numbers.append(i)
        else:
            numbers.append(numbers[i - 2] + numbers[i - 1])


one(10)
