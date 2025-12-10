with open('./input.txt', 'r') as file:
    input = file.read().split('\n')

coordinates = set()

for y_index, line in enumerate(input):
    for x_index, char in enumerate(line):
        if char == "@":
            coordinates.add((x_index, y_index))

neighbour_offsets = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}

def calculate_neighbouring_coordinates(x, y):
    return [(x + dx, y + dy) for dx, dy in neighbour_offsets]

def has_too_many_neighbours(x, y):
    neighbours = calculate_neighbouring_coordinates(x, y)
    matches = 0

    for item in neighbours:
        if item in coordinates:
            matches += 1
            if matches > 3:
                return True
    
    return False

# Part 1

result1 = 0

for y_index, line in enumerate(input):
    for x_index, char in enumerate(line):
        if char != "@":
            continue
        
        if not has_too_many_neighbours(x_index, y_index):
            result1 += 1

print("RESULT 1: ", result1)

# Part 2

input_copy = list(input)

result2 = 0

while True:
    previous_result = result2

    for y_index, line in enumerate(input_copy):
        for x_index, char in enumerate(line):
            if char != "@":
                continue
            
            if not has_too_many_neighbours(x_index, y_index):
                result2 += 1
                
                input_copy[y_index] = input_copy[y_index][:x_index] + "." + input_copy[y_index][x_index + 1:]
                coordinates.remove((x_index, y_index))
    
    if result2 == previous_result:
        break

print("RESULT 2: ", result2)