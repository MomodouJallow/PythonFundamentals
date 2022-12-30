## creating a dictionary literal
capitals = {
    "California": "Sacramento",
    "New York": "Albany",
    "Texas": "Austin"
    }

## creating a dictionary using the dict() function on a tuple
tup = (("Sam", 78455671), ("John", 3126269), ("Tima", 755997823))

phonebook = dict(tup)
print(phonebook)

## Accessing Dictionary Values
## To access a value in a dictionary, enclose the corresponding key in
## square brackets ([ and ]) at the end of dictionary or
## a variable nameassigned to a dictionary

print(capitals["Texas"])
print(phonebook["John"])


## Adding Values in a Dictionary

capitals["Colorado"] = "Denver"  ## adds Colorado:Denver to the dict
capitals["Gambia"] = "Banjul"
print(capitals)

## Removing Values in a Dictionary
## To remove an item from a dictionary, use the del keyword with the key for the value you want to delete

del capitals["Gambia"]
print(capitals)


## Iterating Over Dictionaries
for key in capitals:
    print(key)  ## prints only the keys

print()

for state in capitals:
    print(f"The capital of {state} is {capitals[state]}.")

print()
print(capitals.items())  ## returns a list of tuples of states and their corresponding capitals


















