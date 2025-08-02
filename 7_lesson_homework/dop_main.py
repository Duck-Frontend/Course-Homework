# pylint: skip-file

"""13 и 14 задания которые я не сдал"""
def one(matrix):

    if not matrix:
        return (0, 0)
    
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    sum_main = 0
    sum_secondary = 0
    
    for i in range(rows):
        for j in range(cols):

            if i == j:
                sum_main += matrix[i][j]

            if i + j == cols - 1:
                sum_secondary += matrix[i][j]
    
    return (sum_main, sum_secondary)


def two(matrix):

    new_matrix = []

    for row in matrix:
        count_ones = sum(row)
        new_row = row.copy()

        if count_ones % 2 != 0:
            new_row. append(1)
        else:
            new_row.append(0)

        new_matrix.append(new_row)

    return new_matrix
