from sys import argv

# Pobiera nazwę pliku przy uruchamianiu skryptu
script, filename = argv
# Otwiera plik i przypisuje objekt pliku do zmiennej txt
txt = open(filename)

# Wyświtla komuniakt z przekazaną nazwą pliku w parametrze
print(f"Oto Twój plik {filename}:")
# Wykonuję medodę dla odczytania pliku na zmiennej(objekcie pliku)
print(txt.read())

# Pobiera nazwę pliku w trakcie skryptu
print("Wpisz ponownie nazwę pliku:")
file_again = input("> ")
# Otwiera plik i przypisuje objekt pliku do zmiennej txt_again
txt_again = open(file_again)
# Wykonuję medodę dla odczytania pliku na nowej zmiennej txt_again(objekcie pliku)
print(txt_again.read())
# Zamyka plik
txt_again.close()
