def unique_elements (given_list):
    unique = set(given_list)
    duplicate_set = set()
    for element in given_list:
        if given_list.count(element) > 1:
            duplicate_set.add(element)
    return len(unique), len(duplicate_set)


input_list = input().split()
print(unique_elements(input_list))
