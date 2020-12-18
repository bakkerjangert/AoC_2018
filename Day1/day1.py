# Advent of Code 2018 - Day 1 part a

with open('input.txt') as f:
    lines = f.read().splitlines()

for line in range(len(lines)):
    lines[line] = int(lines[line])

print(' The answer to Day 1 part a is', sum(lines))

# Day 1 part b

result_list = []
temp_result = 0
found = False
i = 0

while True:
    for number in lines:
        temp_result = temp_result + number
        if temp_result in result_list:
            found = True
            print(temp_result)
            break
        result_list.append(temp_result)
    if found == True:
        break
    i += 1
    print('iteration', i)

print('The answer to Day 1 part b is', temp_result)

print('End Of Code')
