def fibonacci_string (num):
    if num == 0:
        return []
    else:
        if num == 1:
            return [0]
        else:
            if num == 2:
                return [0, 1]
            else:
                fibo = [0, 1]
                for i in range(2, num):
                    next_num = fibo[i - 1] + fibo[i - 2]
                    fibo.append(next_num)
                return fibo


input_number = input()
print(fibonacci_string(int(input_number)))
