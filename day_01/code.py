with open('./input.txt', 'r') as file:
    input = file.read().split('\n')

dial_position = 50
result1 = 0

# Part 1

for item in input:
    if not item:
        continue

    rotation_number = int(item[1:]) if item[0] == "R" else -int(item[1:])

    dial_position = (dial_position + rotation_number) % 100
    
    if dial_position == 0:
        result1 += 1

print("PART 1: ", result1)

# Part 2

dial_position = 50
result2 = 0
direction = "R"

for item in input:
    if not item:
        continue

    rotation_number = int(item[1:])

    if item[0] != direction and dial_position != 0:
        dial_position = 100 - dial_position
        
    result2 += (dial_position + rotation_number) // 100

    dial_position = (dial_position + rotation_number) % 100
    
    direction = item[0]

print("PART 2: ", result2)