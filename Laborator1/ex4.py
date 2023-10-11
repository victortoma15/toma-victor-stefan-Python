input_string = input()
output_string = ""

for index in input_string:
    if index == index.lower():
        output_string = output_string + index.lower()
    else:
        output_string = output_string + "_" + index.lower()
print(output_string[1:])