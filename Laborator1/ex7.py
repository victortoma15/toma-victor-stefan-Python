def number_extractor (text):
    number = 0
    is_ok = False

    for index in input_string:
        if is_ok == True:
            if index.isdigit():
                number = number * 10 + int(index)
            else:
                break
        if not is_ok:
            if index.isdigit():
                number = number * 10 + int(index)
                is_ok = True
    return number


input_string = input()
print(number_extractor(input_string))
