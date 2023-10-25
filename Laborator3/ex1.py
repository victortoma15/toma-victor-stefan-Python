def operations (a, b):
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    a_difference = list(set(a) - set(b))
    b_difference = list(set(b) - set(a))

    return intersection, union, a_difference, b_difference


input_a = input()
input_b = input()

print(operations(input_a, input_b))
