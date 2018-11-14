#przypisanie zmiennej
types_of_people = 10
#przekazanie zmiennej w łańcuchu znaków  - 1 i przypisanie do innej zmiennej x
x = f"Istnieje {types_of_people} rodzajów ludzi."

#przypisanie kolejnych zmiennych
binarny = "binarny"
do_not = "nie znają"
#umieszczenie zmiennych string w środku innego łancucha znaków - 2,3 i przypisanie do innej zmiennej y
y = f"Ci, którzy znają system {binarny} i ci, którzy go {do_not}."

#Wyświetlenie łańcuchów znaków
print(x)
print(y)

# wyświetleenie zmiennej x i y w środku kolejnych łańcuchów znaków
print(f"Powiedziałem: {x}")
print(f"Powiedziałem również: '{y}'")

#przypisanie wartości boolean do zmiennej
hilarious = False

# nadanie możliwości późniejszego przekazania  zmiennej  w łańcuchu znaków
joke_evaluation = "Czyż to nie jest przezabawny dowcip?! {}"

#przekazanie formatowanej zmiennej do zarezerwowanego miejsca w łańcuchu znaków w zmiennej joke_evaluation
print(joke_evaluation.format(hilarious))

#przypisanie stringów do zmiennych
w = "To jest lewa strona..."
e = "łańcucha znaków z prawą stroną."

#dodawanie stringów
print(w + e)
