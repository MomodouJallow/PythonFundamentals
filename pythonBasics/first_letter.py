try:
	password = input("Tell me your password: ")
	first_letter_of_password = password[0]
	first_letter_of_password = first_letter_of_password.upper()
	print("The first letter you entered was:" , first_letter_of_password)
except IndexError:
	print("You did not enter password!")