def most_common_letter ():
    text = input()
    text = text.lower()
    dict = {}

    for char in text:
        if char.isalpha():
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1

    max_occurrences = max(dict, key=dict.get)
    print(max_occurrences)


most_common_letter()
