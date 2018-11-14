#Przypisnie wartości do zmiennych
#Ilość samochodów
cars = 100
#Ilość miejsc siedzoncych
space_in_a_car = 4
#Ilość kierowców
drivers = 30
#Ilość pasażerów
passengers = 90
#Ilość samochodów dla których nie ma kierowców
cars_not_driven = cars - drivers
#Ilość samochodów z kierowcą
cars_driven = drivers
#Ile osób mogą zmieścić samochody z kierowcą
carpool_capacity = cars_driven * space_in_a_car
#Średnia Ilość osób do zmiwszczenia w samochodzie
avarage_passangers_per_car = passengers / cars_driven

#Wyświetlenie wyników obliczeń z opisem
print("Dostępnych jest", cars, "samochodów.")
print("Dostępnych jest tylko", drivers, "kierowców.")
print("Dziś będzie", cars_not_driven, "pustych samochodów.")
print("Dziś możemy przetransportować", carpool_capacity, "osób.")
print("Mamy dziś do przewiezienia", passengers, "pasażerów.")
print("Musimy umieścić średnio", avarage_passangers_per_car, "osoby w każdym samochodzie.")
