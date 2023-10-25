def operations(*given_sets):
    operations_dict = {}
    for i in range(len(given_sets)):
        for j in range(i + 1, len(given_sets)):
            operations_dict[str(given_sets[i]) + " | " + str(given_sets[j])] = given_sets[i] | given_sets[j]
            operations_dict[str(given_sets[i]) + " & " + str(given_sets[j])] = given_sets[i] & given_sets[j]
            operations_dict[str(given_sets[i]) + " - " + str(given_sets[j])] = given_sets[i] - given_sets[j]
            operations_dict[str(given_sets[j]) + " - " + str(given_sets[i])] = given_sets[j] - given_sets[i]
    return operations_dict


print(operations({1, 2, 3}, {2, 3, 4}, {3, 4, 5}))
