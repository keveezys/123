#2. Задана квадратная матрица. Получить транспонированную матрицу (перевернутую относительно главной диагонали) и вывести на экран.
def transpose_matrix(matrix):
   transposed_matrix = [list(row) for row in zip(*matrix)]
    return transposed_matrix
square_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed_result = transpose_matrix(square_matrix)
for row in transposed_result:
    print(row)