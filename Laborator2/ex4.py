def beethoven(notes, moves, start):
    song_list = notes[:]
    result = [song_list[start]]
    for index in moves:
        start += index
        if start > len(song_list) - 1:
            start = start % len(song_list)
        result.append(song_list[start])
    return result


print(beethoven(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
