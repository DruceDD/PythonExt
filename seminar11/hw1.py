# Создайте класс Матрица. Добавьте методы для:
# - вывода на печать,
# - сравнения,
# - сложения,
# * умножения матриц

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * cols for _ in range(rows)]

    def __str__(self):
        result = ""
        for row in self.matrix:
            result += " ".join(str(element) for element in row)
            result += "\n"
        return result

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                return False
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        return False
            return True
        return False

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("Матрицы должны иметь одинаковые размеры для сложения")
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return result
        raise TypeError("Неподдерживаемый тип операнда".format(type(other).__name__))

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице.")
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return result
        raise TypeError("Неподдерживаемый тип операнда".format(type(other).__name__))


matrix1 = Matrix(3, 3)
matrix1.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix2 = Matrix(3, 3)
matrix2.matrix = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print(matrix1)
print(matrix2)

if matrix1 == matrix2:
    print("Матрицы равны!\n")
else:
    print("Матрицы не равны!\n")

sum_matrix = matrix1 + matrix2
print(sum_matrix)

product_matrix = matrix1 * matrix2
print(product_matrix)