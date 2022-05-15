# Program for reading files.
print("Input file name in this directory for showing.")
f = str(input("> "))
file = open(f , 'r')
print(file.read())
