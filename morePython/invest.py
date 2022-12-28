def invest(amount , rate , years):
    """Display year on year growth of an initial investment"""
    for year in range(1, number_of_years +1):
        total = amount * ((rate + 1) ** year)
        print(f"Year{year}: ${total:.2f}")
    


amount = float(input("Enter amount: "))
rate = float(input("Enter rate: "))
number_of_years = int(input("Enter number of years: "))

# call function
invest(amount, rate, number_of_years)


       
