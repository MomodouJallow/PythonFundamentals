print("AAA".find("a"))

text = "Somebody say something to Samantha."
new_text = text.replace("s" , "x")
print(new_text)

quote = "INTELLIGENCE\n\
 IS THE\n\
 ABILITY\n\
 TO ADAPT TO\n\
 CHANGE\n\
 -STEPHEN HAWKING"
new_quote = quote.replace("I" , "1")
new_quote = new_quote.replace("T" , "7")
new_quote = new_quote.replace("E" , "3")
new_quote = new_quote.replace("A" , "4")
new_quote = new_quote.replace("O" , "0")
new_quote = new_quote.replace("S" , "5")

print(new_quote)

secret = input("What is your little secret? ")
print(secret.find("a"))