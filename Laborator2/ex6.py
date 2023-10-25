def element_finder (x, *lists):
    element_count = {}

    for input_list in lists:
        for item in input_list:
            if item in element_count:
                element_count[item] += 1
            else:
                element_count[item] = 1

    result = [item for item, count in element_count.items() if count == x]

    return result


list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [4, 5, 6]
list4 = [4, 1, "test"]
x_input = 2

result_output = element_finder(x_input, list1, list2, list3, list4)
print(result_output)
