def previous_list (mapping):
    the_list = []
    key_index = "start"
    while key_index not in the_list:
        the_list.append(key_index)
        key_index = mapping[key_index]
    return the_list


print(previous_list({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
