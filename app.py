## formatted strings
first_name = "Muhammad"
last_name = "Galleh"
msg = f"{first_name} [{last_name}] is a coder!"
print(msg)

print()

## String methods
course = "Python for Beginners"
print(course.upper())
print(course.lower())
print(course.title())
print(course.find("Python"))
print(course.endswith("rs"))
print(course.startswith("Python"))
print(course.replace("Python" , "C#"))
print("for" in course)
print(len(course))
print(course)

print()

## conditionals
is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("Lovely weather!")
    print("Enjoy your day")

print()

## computes buyer's downpayement based on whether they've good credit or not
price = 1_000_000
has_good_credit = True

if has_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"Your downpayment is ${down_payment:,.2f}")

print()

## logical operators
has_high_income = False
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

print()

user_name = "Archimedes"

if len(user_name) < 3:
    print("Name must be at least 3 characters")
elif len(user_name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks great!")

print()

## weight coverter
weight = float(input("Enter weight: "))
unit = input("Enter(L)for pounds or(K)kilo: ")

if unit.upper() == "L":
    converter = weight * 0.45
    print(f"You are {converter} kilos: ")
else:
    converter = weight / 0.45
    print(f"You are {converter} pounds")

print()

## while loop
i = 1
while i <= 10:
    print("*" * i)
    i += 1
print("Done")
    



    
    


     

