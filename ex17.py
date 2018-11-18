from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Kopiownaie z {from_file} do {to_file}")

#te rzeczy w jednej linii?
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read()

print(f"Plik wejściowy na ma {len(indata)} bajtów")

print(f"Czy plik wyjsciowy istnieje? {exists(to_file)}")
print("Wciśnij RETURN, aby kontynuować lub CTRL + C, żeby anulować.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("W porządku, zrobione.")

out_file.close()
#in_file.close()
