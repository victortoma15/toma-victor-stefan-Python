def is_vowel(character):
    if character in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        return True
    else:
        return False


words = input().split()

vowel_counter = 0

for word in words:
    for char in word:
        if is_vowel(char):
            vowel_counter = vowel_counter + 1
print(vowel_counter)
