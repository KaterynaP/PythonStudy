from sys import argv

script, filename = argv

print(f"Wymażemy {filename}.")
print("Jeśli tego nie chcesz, wciśnij  CTRL + C (^C).")
# print("Jeśli chcesz, wciśnij RETURN.")

# input("?")

print("Otwieranie pliku...")
target = open(filename, 'w')

print("Wykasowanie pliku. Do widzenia!")
target.truncate()

print("Teraz poproszę o wpisanie trzech linii tekstu.")

line1 = input("Linia 1: ")
line2 = input("Linia 2: ")
line3 = input("Linia 3: ")

print("Zapiszę je w pliku.")

target.write(line1 + "\n"+ line2 +"\n" + line3 +"\n")

print("A na koniec zamykamy plik.")
target.close()


# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists

# 'rt' by default t - text, b - binary