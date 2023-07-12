"""Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц"""


class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(str(elm) for elm in row) + "\n"
        return str(matrix_str)

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.data == other.data
        return False

    def __add__(self, other):
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result
        else:
            raise ValueError

    def __mul__(self, other):
        if isinstance(other, Matrix) and self.cols == other.rows:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        else:
            raise ValueError


A = Matrix(2, 3)
A.data = [[1, 2, 3], [4, 5, 6]]
print(A)

B = Matrix(3, 2)
B.data = [[7, 8], [9, 10], [11, 12]]
print(B)

C = Matrix(2, 2)
C.data = [[1, 2], [3, 4]]

G = Matrix(2, 2)
G.data = [[3, 4], [5, 2]]

print(A == B)  # False
print(A == A)  # True

D = C + G
print(D)

E = A * B
print(E)

E = A * C
print(E)
