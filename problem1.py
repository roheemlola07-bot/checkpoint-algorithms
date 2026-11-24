set1 = [3, 1, 7, 9]
set2 = [2, 4, 1, 9, 3]

total = 0

for x in set1:
    if x not in set2:
        total = total + x

for x in set2:
    if x not in set1:
        total = total + x

print("Sum of distinct elements:", total)