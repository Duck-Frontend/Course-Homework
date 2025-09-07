def one(finish):
    a, b = 0, 1

    for _ in range(finish):
        yield a
        a, b = b, a + b


one(10)
