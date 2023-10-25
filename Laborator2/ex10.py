def truple (*var_list):
    return list(zip(*var_list))


print(truple([1, 2, 3], [5, 7], ["a", "b"], [10, 11, 12]))
print(truple([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))
