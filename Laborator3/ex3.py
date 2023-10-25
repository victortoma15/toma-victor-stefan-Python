def dictionary_comparer (dictionary_a, dictionary_b):
    if len(dictionary_a) != len(dictionary_b):
        return False
    for key in dictionary_a:
        if key not in dictionary_b:
            return False
        if type(dictionary_a[key]) == dict:
            if not dictionary_comparer(dictionary_a[key], dictionary_b[key]):
                return False
        else:
            if dictionary_a[key] != dictionary_b[key]:
                return False
    return True


input_dictionary_a = {
    'name': 'Victor',
    'age': 21,
    'address': {
        'street': 'Iasi',
        'city': 'Iasi',
        'zip': '12345'
    },
    'hobbies': ['sports', 'informatics']
}

input_dictionary_b = {
    'name': 'Victor',
    'age': 21,
    'address': {
        'street': 'Iasi',
        'city': 'Iasi',
        'zip': '12345'
    },
    'hobbies': ['sports', 'informatics']
}
print(dictionary_comparer(input_dictionary_a, input_dictionary_b))
