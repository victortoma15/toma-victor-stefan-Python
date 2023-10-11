def count_words (text):
    count = 1
    for index in range(len(text)):
        if text[index] == ' ':
            count = count + 1

    return count


input_string = input()

print(count_words(input_string))
