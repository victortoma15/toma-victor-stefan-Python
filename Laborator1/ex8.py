def count_ones (number):
    two = 2
    count = 0
    while two < number:
        two = two * 2

    if two == number:
        return 1

    two = two / 2

    while number != 0:
        if number >= two:
            number = number - two
            count = count + 1
        two = two / 2

    return count


print(count_ones(65))
