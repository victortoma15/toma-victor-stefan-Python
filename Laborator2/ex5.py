def replace_with_zero (matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    for index in range(rows):
        for j_index in range(columns):
            if j_index < index:
                matrix[index][j_index] = 0
    return matrix


input_matrix = [[9, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 4, 7],
                [7, 5, 9, 5]]
print(replace_with_zero(input_matrix))
