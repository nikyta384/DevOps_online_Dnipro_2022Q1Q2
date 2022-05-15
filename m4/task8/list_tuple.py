
list_number = str(input("> "))
list_number = list_number.replace(',', '')
list_number = list_number.replace(' ', '')
print("List: " + str(list(list_number)))
print("Tuple: " + str(tuple(list_number)))
