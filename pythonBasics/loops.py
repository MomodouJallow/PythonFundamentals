amount = float(input("Enter amount: "))

for num_people in range(2 , 6):
	print(f"{num_people} people is ${amount / num_people:,.2f} each")