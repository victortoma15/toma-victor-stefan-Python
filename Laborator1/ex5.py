input_matrix = [["f", "i", "r", "s"],
                ["n", "_", "l", "t"],
                ["o", "b", "a", "_"],
                ["h", "t", "y", "p"],
                ]

top = 0
bottom = len(input_matrix) - 1
right = len(input_matrix[0]) - 1
left = 0
while top <= bottom and left <= right:
    for index in range(left, right + 1):
        print(input_matrix[top][index], end="")
    top += 1
    if top <= bottom and left <= right:
        for index in range(top, bottom + 1):
            print(input_matrix[index][right], end="")
        right -= 1
    if top <= bottom and left <= right:
        for index in range(right, left - 1, -1):
            print(input_matrix[bottom][index], end="")
        bottom -= 1
    if top <= bottom and left <= right:
        for index in range(bottom, top - 1, -1):
            print(input_matrix[index][left], end="")
        left += 1