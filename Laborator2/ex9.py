def field_spectators(matrix):
    result = []
    matrix = list(zip(*matrix))
    maxim = 0
    for indexR, row in enumerate(matrix):
        for indexC, column in enumerate(row):
            if column > maxim:
                maxim = column
            else:
                result.append((indexC, indexR))
        maxim = 0
    return result


input_matrix = [[1, 2, 3, 2, 1, 1],
                [2, 4, 4, 3, 7, 2],
                [5, 5, 2, 5, 6, 4],
                [6, 6, 7, 6, 7, 5]]

print(field_spectators(input_matrix))