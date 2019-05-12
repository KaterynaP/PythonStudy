def add(a, b):
    print(f"Dodawanie {a} + {b}")
    return a + b

def substract(a, b):
    print(f"Odejmowanie {a} + {b}")
    return a - b

def multiply(a, b):
    print(f"Mnożenie {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dzielenie {a} / {b}")
    return a / b

print("Wykonajmy kilka opercji aretmytycznych tylko za pomoca funcji")
age = add(30, 5)
height = substract(7, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

#łamigłówka
#print("Oto zadanie")
#what = add(age, substract(height, multiply(weight, divide(iq, 2))))
#print("To daje:", what)

one = divide(iq, 2)
print (one)
two = multiply(weight, one)
three = substract(height, two)
four = add(age, three)
