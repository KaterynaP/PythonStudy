from sys import argv

script, filename = argv

print(f"Wymażemy {filename}.")
print("Jeśli tego nie chcesz, wciśnij  CTRL + C (^C).")
print("Jeśli chcesz, wciśnij RETURN.")

input("?")

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
