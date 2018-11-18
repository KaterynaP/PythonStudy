from sys import argv

skrypt, filename = argv

my_file = open(filename)
text_of_my_file = my_file.read()
print(text_of_my_file)
my_file.close()
