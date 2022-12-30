## Tuples
my_first_tuple = (1, 2, 3)
print(type(my_first_tuple))  ## class: tuple

singleton_tuple = (2,)

## The tuple() Built-in function
string = "Python"
tup = tuple(string)
print(tup)
print(string)  ## unchanged

## tuple methods
print(len(my_first_tuple))  ## returns the number of items in the tuple
print(my_first_tuple[0])  ## returns the first item in the tuple
print(my_first_tuple[:2])  ## returns the first and second items

## tuples are iterable
for item in my_first_tuple:
    print(item)

## tuple unpacking
coordinates = (4.12, 2.67)
x , y = 4.12, 2.67
print(x)
print(y)

## another tuple construction method
name, age, job = "Mo", 24, "Programmer"
print(name)
print(age)
print(job)


## One common use of tuples is to return multiple values from a single function
def adder_subtractor(num1, num2):
    return (num1 + num2, num1 - num2)
    

print(adder_subtractor(3, 2))











    
