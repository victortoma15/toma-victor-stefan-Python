import os
import sys

if len(sys.argv) != 2:
    print("Incearca sa folosesti: python 4.py <path-ul directorului>")
    sys.exit(1)

directory_path = sys.argv[1]

if not os.path.isdir(directory_path):
    print(f"{directory_path} nu este un director.")
    sys.exit(1)

try:
    files = os.listdir(directory_path)
except PermissionError:
    print(f"Nu avem permisiunea de citire {directory_path}.")
    sys.exit(1)

if not files:
    print(f"{directory_path} nu are nimic.")
    sys.exit(0)

extensions = {}

for file in files:
    if os.path.isfile(os.path.join(directory_path, file)):
        extension = os.path.splitext(file)[1]
        if extension in extensions:
            extensions[extension] += 1
        else:
            extensions[extension] = 1

for extension in extensions:
    print(f"{extension}: {extensions[extension]}")

