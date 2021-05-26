names = []
phone_numbers = []
num =5

for x in range(num):
    name = input(" Enter your Name: ")
    phone_number = input("Enter your phoneNumber: ")
    names.append(name)
    phone_numbers.append(phone_number)
print("\nName\t\tphone Number\n")
for x in range(num):
 print("{}\t\t\t{}".format(names[x],phone_numbers[x]))
 search_term = input("\nEnter search Name")
 print("search Results")
 if search_term in names:
     index =names.index(search_term)
     phone_number =phone_numbers[index]
     print("Name {},phone Number: {}".format(search_term,phone_number))
 else: #if you write the name that is not in the contact book
     print("Name not found")