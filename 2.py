x = 1
if x == 2:
    print("x is 2")
# my_name = input("enter your name: ")
# if my_name == "Refael":
#     print("Good!")

a = 4
b = 14
if a < b:
    print("a is lower")
result = 14 ** 3
print(result)
fName = "Refael"
lName = "Admoni"
full_name = fName + " " + lName
another_full_name = "%s %s" % (fName, lName)
another_full_name2 = f"{fName} {lName}"
another_full_name3 = "{} {}".format(fName, lName)
print(another_full_name)
print(another_full_name2)
print(another_full_name3)

my_full_description = "Name: Refael\nage: 30\nMerried: Yes\n\n"
print(my_full_description)

my_full_description = 'Name: "Refael"\nage: 30\nMerried: Yes\n\n'
print(my_full_description)

my_full_description = "Name: \"Refael\"\nage: 30\nMerried: Yes\n\n"
print(my_full_description)
