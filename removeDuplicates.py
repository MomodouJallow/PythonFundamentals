numbers = [2, 3, 3 , 2 , 4 , 5, 6, 5]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number).sort()
print(uniques)
