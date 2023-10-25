def group_by_rhyme(lista):
    result = []
    for index1 in lista:
        for index2 in lista:
            if index1 != index2 and index1[-2:] == index2[-2:]:
                result.append([index1, index2])
                lista.remove(index1)
                lista.remove(index2)
                break
    for index in lista:
        result.append([index])
    return result


input_string = ['ana', 'banana', 'carte', 'arme', 'parte']
print(group_by_rhyme(input_string))
