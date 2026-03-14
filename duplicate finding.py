numbers = [1, 3, 5, 3, 7, 9, 1, 5, 8, 2, 4, 6, 8, 0, 2, 4, 6, 9, 7, 0]  
seen = []
duplicates = []

for number in numbers:
    if number in seen:
        # it's a duplicate — add to duplicates list
        duplicates.append(number)
    else:
        # haven't seen it yet — add to seen list
        seen.append(number)

print("Duplicates:", duplicates)