def operations (a, b):
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    a_difference = list(set(a) - set(b))
    b_difference = list(set(b) - set(a))

    return intersection, union, a_difference, b_difference


a = input()
b = input()

print(operations(a, b))
