name = 'Zed. A. Shaw'
age = 35 #nie kłamię
height = 190 #centymetrów
weight = 80 #kilogramów
eyes = 'Niebieskie'
teeth = 'Białe'
hair = 'Brązowe'
height_in = height * 0.39370 #cale
weight_lb = weight * 2.2046 #funty


print(f"Porozmawiajmy o {name}.")
print(f"Ma {height} centymetrów  albo {round(height_in)} cali wzrostu.")
print(f"Waży {weight} kilogramów albo {round(weight_lb)} funtów.")
print(f"Tak naprawdę nie waży dużo.")
print(f"Ma {eyes} oczy i {hair} włosy.")
print(f"Jego zęby są zazwyczaj {teeth}, w zależnosci od wypitej kawy.")

#ta linia jest trudna, więc wpisuj ją uważnie
total = age + height + weight
print(f"Jeśli dodam {age}, {height} i {weight}, otrzymam {total}.")
