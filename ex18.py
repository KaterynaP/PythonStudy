# ta funkcja jest podobna do skryptów z argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# *args bezcelowo, moze byc tak
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# f-ja z 1 argumentem
def print_one(arg1):
    print(f"arg1: {arg1}")


print_two("Kasia", "Alek")
print_two_again("Pidrushniak", "Dobek")
print_one("Whatever")
