with open('./input.txt', 'r') as file:
    input = file.read().split('\n')

digits = [x for x in range(1, 10)]

# Part 1

result1 = 0

def joltage_finder(data: str):
    obj = {x: [] for x in digits}

    for index, char in enumerate(data):
        digit = int(char)
        obj[digit].append(index)

    for digit in reversed(digits):
        if len(obj[digit]) == 0:
            continue

        for another_digit in reversed(digits):
            if any(x > obj[digit][0] for x in obj[another_digit]):
                return (digit * 10) + another_digit

    return None

for line in input:
    x = joltage_finder(line)
    if x is not None:
        result1 += x

print("RESULT 1: ", result1)

# Part 2

result2 = 0

def match_digit_in_list(list, index0, index1):
    for x in list:
        if index0 <= x <= index1:
            return x
        
    return None
    
def advanced_joltage_finder(data: str):
    answer = ""

    obj = {x: [] for x in digits}

    for index, char in enumerate(data):
        digit = int(char)
        obj[digit].append(index)

    pointer = 0

    for i in range(12):
        for digit in reversed(digits):
            if len(obj[digit]) == 0:
                continue

            a = match_digit_in_list(obj[digit], pointer, (len(data) - 12 + i))
            
            if a is not None:
                answer += str(digit)
                pointer = a + 1
                break
                    
    return int(answer)

for line_index, line in enumerate(input):
    x = advanced_joltage_finder(line)
    if x is not None:
        result2 += x

print("RESULT 2: ", result2)