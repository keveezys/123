#1. Задана матрица порядка n и число к. Разделить элементы k-й строки на диагональный элемент, расположенный в этой строке.
def divide_row_by_diagonal(matrix, k):
    n = len(matrix)
    if k >= n or not matrix[k][k]:
        print("Некорректные входные данные.")
        return
    diagonal_element = matrix[k][k]
    for j in range(n):
        matrix[k][j] /= diagonal_element
matrix = [
    [2, 3, 1],
    [1, 4, 2],
    [3, 6, 5]
]
k = 1
divide_row_by_diagonal(matrix, k)
for row in matrix:
    print(row)