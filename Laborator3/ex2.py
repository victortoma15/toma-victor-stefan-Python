def char_count (given_string):
    char_dictionary = {}
    for char in given_string:
        if char in char_dictionary:
            char_dictionary[char] += 1
        else:
            char_dictionary[char] = 1
    return char_dictionary


input_string = input()
print(char_count(input_string))
