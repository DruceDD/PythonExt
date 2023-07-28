# Напишите функцию для транспонирования матрицы.


def transpose(matrix):
    for i in range(len(matrix)):
         for j in range(len(matrix[0])):
                  new_matrix[j][i] = matrix[i][j]
    return new_matrix


matrix =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(transpose(matrix))