import os
import sys

try:
    directory_path = sys.argv[1]
    total_size = 0

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            total_size += file_size

    print(f"Marime: {total_size} ")

except IndexError:
    print("Eroare la terminal.")

except FileNotFoundError:
    print("Nu s-a gasit.")

except PermissionError:
    print("No access.")

except Exception as e:
    print(f"Error: {e}")


