import random


def one(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return one(arr, target, mid + 1, right)
    else:
        return one(arr, target, left, mid - 1)


def two(n):
    if n == 0:
        return '0'
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary if binary else '0'


def three(n, divisor=None):
    if n <= 1:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return three(n, divisor - 1)


def four(a, b):
    if b == 0:
        return a
    return four(b, a % b)


def five(str, action):
    shift = 3
    new_str = ""
    if action == "зашифровать":
        for i in str:
           new_str += chr(ord(i) + shift)
        return new_str
    if action == "расшифровать":
        for i in str:
           new_str += chr(ord(i) - shift)
        return new_str
    

def six(text, key, action):
    result = ""
    key_length = len(key)
    for i, char in enumerate(text):
        key_char = key[i % key_length]
        shift = ord(key_char)
        if action == "зашифровать":
            result += chr((ord(char) + shift) % 65536)
        elif action == "расшифровать":
            result += chr((ord(char) - shift) % 65536)
    return result 


def seven(m, n, min_val=0, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(m)]


mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
    ]

def eight(mat):
    if not mat or not mat[0]:
        return None, None

    max_val = mat[0][0]
    min_val = mat[0][0]
    max_index = (0, 0)
    min_index = (0, 0)

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > max_val:
                max_val = mat[i][j]
                max_index = (i, j)
            if mat[i][j] < min_val:
                min_val = mat[i][j]
                min_index = (i, j)

    return max_index, min_index
    

def nine(matrix):
    total = 0
    for row in matrix:
        for num in row:
            total += num
    
    if total == 0:
        return []
    
    result = []
    for j in range(len(matrix[0])):
        col_sum = 0
        for row in matrix:
            col_sum += row[j]
        percent = (col_sum / total) * 100
        result.append(round(percent, 1))
    
    return result


def ten(matrix, k):
    new_matrix = []
    for row in matrix:
        new_row = []
        for j in range(len(row)):
            new_row.append(row[j] * row[k])
        new_matrix.append(new_row)
    return new_matrix


def eleven(matrix, l):
    new_matrix = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
            new_row.append(matrix[i][j] + matrix[l][j])
        new_matrix.append(new_row)
    return new_matrix


def twelve(matrix, h):
    columns_with_h = []
    columns_without_h = []
    
    for j in range(len(matrix[0])):
        found = False
        for row in matrix:
            if row[j] == h:
                found = True
                break
                
        if found:
            columns_with_h.append(j)
        else:
            columns_without_h.append(j)
            
    return columns_with_h, columns_without_h
    


