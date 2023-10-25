def ascii_flag (x, string_list, flag):
    return_list = []

    for string in string_list:
        almost_result = []

        if flag == True:
            for char in string:
                if char.isalpha and ord(char) % x == 0:
                    almost_result.append(char)
        else:
            for char in string:
                if char.isalpha and ord(char) % x != 0:
                    almost_result.append(char)

        return_list.append(almost_result)

    return return_list


number_input = int(input())
string_input = input().split()
flag_input = input()
print(ascii_flag(number_input, string_input, flag_input))