def transpose(mat: list[list[float | int]]) -> list[list]:
    # Проверка, что матрица не пустая
    if not mat:
        return []

    # Проверка, что все элементы - списки
    if not all(isinstance(row, list) for row in mat):
        raise TypeError("Все элементы должны быть списками")

    # Проверка на прямоугольность
    length = len(mat[0])
    for row in mat:
        if length != len(row):
            raise ValueError("рваная матрица")

    rows = len(mat)
    cols = length

    # Создаём транспонированную матрицу
    tr_mat = []
    for _ in range(cols):
        tr_mat.append([0] * rows)

    # Заполняем транспонированную матрицу
    for i in range(rows):
        for j in range(cols):
            tr_mat[j][i] = mat[i][j]

    return tr_mat


def row_sums(mat: list[list[float | int]]) -> list[float]:
    # Проверка на пустую матрицу
    if not mat:
        return []

    # Проверка, что все элементы - списки
    if not all(isinstance(row, list) for row in mat):
        raise TypeError("Все элементы должны быть списками")

    # Проверка на прямоугольность
    length = len(mat[0])
    for row in mat:
        if length != len(row):
            raise ValueError("рваная матрица")

    return [sum(row) for row in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    # Проверка на пустую матрицу
    if not mat:
        return []

    # Проверка, что все элементы - списки
    if not all(isinstance(row, list) for row in mat):
        raise TypeError("Все элементы должны быть списками")

    # Проверка на прямоугольность
    length = len(mat[0])
    for row in mat:
        if length != len(row):
            raise ValueError("рваная матрица")

    num_cols = length
    result = [0] * num_cols

    for row in mat:
        for i, val in enumerate(row):
            result[i] += val

    return result


# print("=== transpose ===")
# print(transpose([[1, 2, 3]]))
# print(transpose([[1], [2], [3]]))
# print(transpose([[1, 2], [3, 4]]))
# print(transpose([]))
# print(transpose([1, 2, 3]))

# print("\n=== row_sums ===")
# print(row_sums([[1, 2, 3], [4, 5, 6]]))
# print(row_sums([[-1, 1], [10, -10]]))
# print(row_sums([[0, 0], [0, 0]]))
# print(row_sums([[1, 2], [3]]))

# print("\n=== col_sums ===")
# print(col_sums([[1, 2, 3], [4, 5, 6]]))
# print(col_sums([[-1, 1], [10, -10]]))
# print(col_sums([[0, 0], [0, 0]]))
# print(col_sums([[1, 2], [3]]))
