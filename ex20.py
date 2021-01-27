from sys import argv

script, input_file = argv


# definicaj f-ji
def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())


# przypisanie pliku podanego przy wywołaniu tego skryptu do zmiennej current_file
current_file = open(input_file)

print("Najpierw wydrukujmy cały plik:\n")

# wywołanie funkcji napisanej wcześniej z parametrem (drukuje wszystkie trzy linie)
print_all(current_file)

print("Teraz przewińmy do tyłu, tak jak przewija się kasetę.")

# wywołanie funkcji napisanej wcześniej z parametrem(przewija na początek pliku)
rewind(current_file)

print("Wydrukujmy trzy linie:")

# przypisanie int do zmiennej
current_line = 1
# wywołanie funkcji napisanej wcześniej z parametrami 1 i aktualny plik od poczatku
print_a_line(current_line, current_file)

current_line = current_line + 1  # current_line = 2
print_a_line(current_line, current_file)

current_line = current_line + 1  # current_line = 2 + 1 = 3
print_a_line(current_line, current_file)
