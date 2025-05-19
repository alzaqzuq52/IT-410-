# Name: Hassan

# Problem 5-1: Conditional Tests
# I predict the expression below will evaluate to True
name = "Hassan"
print(name == "Hassan")

# I predict the expression below will evaluate to False
age = 25
print(age > 30)

# I predict the expression below will evaluate to True
is_student = True
print(is_student == True)

# I predict the expression below will evaluate to False
grade = "B"
print(grade == "A")

# I predict the expression below will evaluate to True
price = 5.99
print(price < 10)

# I predict the expression below will evaluate to False
items = ["apple", "banana"]
print("orange" in items)

# Problem 5-2: Odd number test
number1 = 5
if number1 % 2 != 0:
    print(str(number1) + " is an odd number.")

number2 = 6
if number2 % 2 != 0:
    print(str(number2) + " is an odd number.")  # This won't run

# Problem 5-3: If-Else version
number = 15
if number % 2 != 0:
    print(str(number) + " is an odd number.")
else:
    number += 1
    print("Number is even. Now increased to:", number)

# Problem 5-4: Favorite fruits and list length check
favorite_fruits = ["apple", "banana", "strawberry"]

if len(favorite_fruits) == 2:
    print("You like two fruits.")
elif len(favorite_fruits) == 3:
    print("You like three fruits.")
elif len(favorite_fruits) == 4:
    print("You like four fruits.")
elif len(favorite_fruits) >= 5:
    print("You like several fruits.")

# Problem 5-5: Check if values in list
num_list = list(range(1, 56))
a = 5
b = 15

if a in num_list:
    print(str(a) + " was found in the list.")
else:
    print(str(a) + " was not found in the list.")

if b in num_list:
    print(str(b) + " was found in the list.")
else:
    print(str(b) + " was not found in the list.")

# Problem 5-6: Store sales check
favorite_stores = ["Abercrombie", "Macys", "Fanatics", "Nike"]
sale_stores = ["Target", "Amazon", "Macys", "Nike"]

for store in favorite_stores:
    if store in sale_stores:
        print("Take advantage of the sale at", store + "!")
    else:
        print(store + " isn't currently running a sale.")




