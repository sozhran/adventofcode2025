import math

input = open('./input.txt', 'r').read().split(',')

# Part 1

ids_to_check = []
result1 = 0

for item in input:
    [num1, num2] = item.split('-')

    for x in range(int(num1), int(num2) + 1):
        x = str(x)
        if len(x) % 2 == 0:  # odd length numbers will never satisfy the condition
            ids_to_check.append(x)

for id in ids_to_check:
    midpoint = int(len(id) / 2)
    
    if id[midpoint:] == id[:midpoint]:
        result += int(id)

print("RESULT 1: ", result1)

# Part 2

ids_to_check = []
result2 = 0

for item in input:
    [num1, num2] = item.split('-')

    for x in range(int(num1), int(num2) + 1):
        ids_to_check.append(str(x))

for id in ids_to_check:
    for i in range(1, math.floor(len(id) / 2) + 1):
        if len(id) % i == 0 and id == id[:i] * int(len(id) / i ):
            result2 += (int(id))
            break

print("RESULT 2: ", result2)