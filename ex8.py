#przypisanie ciągu znaków (gdzie będziemy przekazywać zmienne) do zniennej
formatter = "{} {} {} {}"

#przekazanie w funkcji integery
print(formatter.format(1, 2, 3, 4))
#przekazanie w funkcji stringi
print(formatter.format("jeden", "dwa", "trzy",  "cztery"))
#przekazanie w funkcji boolean
print(formatter.format(True, False, True, False))
#przekazanie w funkcji samą zmienną
print(formatter.format(formatter, formatter, formatter, formatter))
#przekazanie w funkcji łańcuchy znakowe
print(formatter.format(
    "Spróbuj tutaj",
    "Wpisać własny tekst",
    "Może wiersz",
    "Albo piosenkę o lęku"
))
