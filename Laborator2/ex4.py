def beethoven(notes, moves, start):
    start = int(start) % len(notes)

    final_song = []

    for index in moves:
        index = int(index)
        start = (start + index) % len(notes)
        final_song.append(notes[start])

    return final_song


notes_input = input().split()
moves_input = input().split()
start_input = input()
print(beethoven(notes_input, moves_input, start_input))
