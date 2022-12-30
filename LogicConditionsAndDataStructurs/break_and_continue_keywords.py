## The "break" keyword
while True:
    character = input("Enter a character: ")
    if character == "q" or character == "Q":
        break
print("Thank you.")


## The "continue" keyword
for n in range(1 , 50):
    if n % 3 == 0:
        continue
    print(n)
