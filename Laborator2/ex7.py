def is_palindrome (number):
    return number == number[::-1]


def palindrome_tuple (number_list):
    counter = 0
    greatest_palindrome = -1
    for index in range(len(number_list)):
        if is_palindrome(number_list[index]):
            counter = counter + 1
            if int(number_list[index]) > greatest_palindrome:
                greatest_palindrome = int(number_list[index])
    return [counter, greatest_palindrome]


input_list = input().split()
print(palindrome_tuple(input_list))
