import os
import sys

try:
    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    if not os.path.isdir(directory_path):
        raise Exception("PATH INVALID")

    for filename in os.listdir(directory_path):
        if filename.endswith(file_extension):
            file_path = os.path.join(directory_path, filename)
            try:
                with open(file_path, "r") as file:
                    contents = file.read()
                    print(contents)
            except:
                print(f"Eroare la fisiere: {file_path}")
except:
    print("Try again")

