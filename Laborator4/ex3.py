class Matrix:
    def __init__ (self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0] * m for i in range(n)]

    def get_matrix (self):
        return self.matrix

    def set_matrix (self, matrix):
        if len(matrix) != self.n or len(matrix[0]) != self.m:
            return None
        self.matrix = matrix

    def get_cell (self, i, j):
        return self.matrix[i][j]

    def set_cell (self, i, j, value):
        self.matrix[i][j] = value

    def transpose (self):
        num_rows = len(self.matrix)
        num_columns = len(self.matrix[0])
        transposed = [[self.matrix[j][i] for j in range(num_rows)] for i in range(num_columns)]
        return transposed

    def multiply_matrices (self, other):
        if self.m != other.n:
            return None

        new_matrix = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                x = 0
                for k in range(self.m):
                    x += self.get_cell(i, k) * other.get_cell(k, j)
                new_matrix.set_cell(i, j, x)

        return new_matrix

    def use_lambda_function (self, lambda_function):
        for i in range(self.n):
            for j in range(self.m):
                new_val = lambda_function(self.get_cell(i, j))
                self.set_cell(i, j, new_val)
        return self


input_matrix = Matrix(3, 3)
input_matrix.set_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
input_matrix.use_lambda_function(lambda x: x * 2)
print(input_matrix.get_matrix())
