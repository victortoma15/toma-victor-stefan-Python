def is_palindrome(x):
    string_x = str(x)

    if string_x == string_x[::-1]:
        return True
    else:
        return False


input_x = input()
if is_palindrome(input_x):
    print("It is a palindrome")
else:
    print("It's not a palindrome")