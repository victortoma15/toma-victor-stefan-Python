def is_prime (number):
    number = int(number)
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    index = 3

    while index * index <= number:
        if number % index == 0:
            return False
        index += 2
    return True


def find_prime (l):
    primes = []
    for index in l:
        if is_prime(index):
            primes.append(index)
    return primes


input_list = input().split()
print(find_prime(input_list))
