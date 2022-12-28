def convert_cel_to_far(C):
    """Converts temperature from degrees celsius to degrees fahrenheit"""
    return C * 9/5 + 32


def convert_far_to_cel(F):
    """Converts temperature from degrees fahrenheit to degrees celsius"""
    return (F - 32) * 5/9


choice = input("""
Enter F to convert Fahrenheit to celsius
Enter C to convert Celsius to Fahrenheit: """)

choice = choice.upper()
if choice == "F":
    far_temp = float(input("Enter temp in degrees F: "))
    result = convert_far_to_cel(far_temp)
    print(f"{far_temp} degrees F = {result:.2f} degrees C")
elif choice == "C":
    cel_temp = float(input("Enter temp in degrees C: "))
    result = convert_cel_to_far(cel_temp)
    print(f"{cel_temp} degrees F = {result:.2f} degrees F")
else:
    print("Error!")


