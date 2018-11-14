from sys import argv

script, first, second, third = argv

#podanie zmiennych jako argumentów
print("Ten skrypt nazywa się:", script)
print("Pierwsza zmienna to:", first)
print("Druga zmienna to:", second)
print("Trzecia zmienna to:", third)

#podanie zmiennych w inpucie sposob 1
fourth = input("Podaj czwartą zmienna: ")
print(f"Czwarta zmienna to: {fourth}")
#print("Czwarta zmienna to: " + fourth)

#podanie zmiennych w inpucie sposob 2
print ("Piąta zmienna to: " + input("Podaj piąta zmienna: "))
