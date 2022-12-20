def convert_cel_to_far(C):
	"""Takes in celcius temperature and converts it to fahrenheit"""
	return C * 9 / 5 + 32


def convert_far_to_cel(F):
	"""Takes in Fahrenheit temperature and converts it to degrees celcius"""
	return (F - 32) * 5 / 9



celcius = float(input("Enter Celcius temperature: "))
F_temp = convert_cel_to_far(celcius)
print(f"{celcius} degrees celcius = {F_temp:.2f} degrees Fahrenheit.")

fahrenheit = float(input("Enter Fahrenheit temperature: "))
C_temp = convert_far_to_cel(fahrenheit)
print(f"{fahrenheit} degrees Fahrenheit = {C_temp:.2f} degrees Celsius.")

