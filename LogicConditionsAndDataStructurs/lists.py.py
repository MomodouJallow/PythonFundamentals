## List literal
my_color = ["red", "yellow", "green", "blue"]

## the list() built_in function
my_num = "1234"
new_list = list(my_num)
print(new_list)

## using the string object’s .split() method
groceries = "eggs, milk, cheese"
groceries_list = groceries.split(",")
print(groceries_list)

## Split string on semi-colons
alph = "a;b;c"
alph_list = alph.split(";")
print(alph_list)

## Split string on spaces
say = "The quick brown fox jumps over the lazy dog"
say_list = say.split(" ")
print(say_list)

## Split string on multiple characters
word = "abbaabba"
word_list = word.split("ba")
print(word_list)

## Basic List Operations

## indexing
numbers = [1, 3, 6, 10, 13, 16, 19, 22]
print(numbers[2])  ## prints 6 which is the element at index 2

## list slicing
print(numbers[2:6])

## check existence of item in list
print(13 in numbers)  ## prints True

## lists are iterable
for number in numbers:
    print(number)

print()
## print only the even numbers in the list
for number in numbers:
    if number % 2 == 0:
        print(number)


print()

## mutate lists
fruits = ["kiwi", "orange", "apple", "banana", "mango"]
fruits[2] = "pineapple"
print(fruits)

print()

## mutiple updates
fruits[0:2] = ["melon", "peach"]
print(fruits)

print()

## List Methods For Adding  Elements
countries = []  ## empty
countries.append("Gambia")  ## adds Gambia to the list countries
countries.append("Uganda")
countries.append("USA")
countries.append("Spain")
print(countries)

## list.insert(index, item) method adds item to a specified index in the list
countries.insert(1, "Canada")
print(countries)

## The list.extend() method is used to add several new elements to the end of a list
countries.extend(["England", "France"])
print(countries)

print()
##List Methods For Removing  Elements
countries.pop()  ## removes the last item from the list -> France
print(countries)
countries.pop(2)  ## removes the item at index 2 -> Uganda
print(countries)

countries.remove("Gambia")  ## literally removes Gambia from the list
print(countries)

print()

## methods for lists containing numbers only
number_list = [1, 2, 7, 4, 14, 6]
print(sum(number_list))  ## adds all the numbers and return the total
print(max(number_list))  ## returns the greatest number in the list -> 14
print(min(number_list))  ## returns the smallest number in the list -> 1

print()

## List Comprehensions
string = "eggs, fruit, orange juice"
breakfast = string.split(",")
print(len(breakfast))

lengths = [len(item)for item in breakfast]  ## list comprehension syntax
print(lengths)

## sort()
cars = ["Subaru", "Audi", "BMW", "Toyota" ]
cars.sort()  ## sorts the list permanently in ascending order
print(cars)

## sort() in reverse order. syntax: list.sort(reverse = True)
continents = ["Europe", "Africa", "America", "Australia", "Asia"]
continents.sort(reverse = True) ## sorts permanently in decending order
print(continents)

## sorting using a key
names = ["harry", "John", "sam", "Tima"]
names.sort(key = len)
print(names)

print()

## sort a list temporarily using the sorted(list) function
grades = ["A", "E", "F", "C", "D" , "B"]

print("Here is the original list: ")
print(grades)

print("\nHere is the sorted list:")
print(sorted(grades))

print("\nHere is the original list again:")
print(grades)

print()

## reverse the chronological order of a list using the reverse() function
grades.reverse()
print(grades)




















