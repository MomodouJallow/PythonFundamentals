num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
difference = num1 - num2
check_difference = difference.is_integer()
print(f"The difference between {num1} and {num2} is an integer? {check_difference}")