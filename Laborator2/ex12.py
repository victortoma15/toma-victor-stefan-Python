def group_by_rhyme(string_list):
    rhymed_list = []
    for string_i in range(len(string_list)):
        rhyme = False
        current_string = string_list[string_i]
        group = [current_string]
        for string_j in range(string_i + 1, len(string_list)):
            next_string = string_list[string_j]
            if current_string[-2:] == next_string[-2:]:
                group.append(next_string)
                rhyme = True

        if not rhyme:
            rhymed_list.append([current_string])
        else:
            rhymed_list.append(group)
    return rhymed_list


input_string = ['ana', 'banana', 'carte', 'arme', 'parte']
print(group_by_rhyme(input_string))
