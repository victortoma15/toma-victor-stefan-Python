def sort_by_3rd (tuples_list):
    for i in range(1, len(tuples_list)):
        current_tuple = tuples_list[i]
        j = i - 1

        while j >= 0 and (
                len(current_tuple) < 2 or len(current_tuple[1]) < 3 or current_tuple[1][2] < tuples_list[j][1][2]):
            tuples_list[j + 1] = tuples_list[j]
            j -= 1

        tuples_list[j + 1] = current_tuple

    return tuples_list


tuples_input = [('abc', 'bcd'), ('abc', 'zza')]
print(sort_by_3rd(tuples_input))
