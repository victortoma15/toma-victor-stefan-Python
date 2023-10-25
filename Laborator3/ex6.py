def unique_elements (given_list):
    unique_a = set(given_list)
    unique_b = set()
    for element in given_list:
        if given_list.count(element) > 1:
            unique_b.add(element)
    return len(unique_a), len(unique_b)


input_list = input().split()
print(unique_elements(input_list))
