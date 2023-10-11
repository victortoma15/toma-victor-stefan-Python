def GCD (a, b):
    if b == 0:
        return a
    return GCD(int(b), int(a % b))


nr = input().split()

ini_gcd = GCD(int(nr[0]), int(nr[1]))

for index in nr:
    true_gcd = GCD(int(index), int(ini_gcd))

print(int(true_gcd))
