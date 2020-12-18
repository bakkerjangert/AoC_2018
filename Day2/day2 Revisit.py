# Advent of Code 2018 - Day 2 Part 1 and Part 2
with open('input.txt') as f:
    lines = f.read().splitlines()

# Part 1
count_2 = 0
count_3 = 0

# Place each line in alphabetical order and count letters; break if 2 and 3 letters are found for optimisation
for line in lines:
    found_2, found_3 = False, False
    string = ''.join(sorted(line))
    index = 0
    while index < len(string):
        val = string.count(string[index])
        if val == 2 and not found_2:
            count_2 += 1
            found_2 = True
        if val == 3 and not found_3:
            count_3 += 1
            found_3 = True
        if found_2 and found_3:
            break
        index += val

print(f'\n---Part 1---\n')
print(f'The answer to Part 1 is {count_2} x {count_3} = {count_2 * count_3}')

# Part 2
# Assumptions:
# --> All strings are of equal length
# --> Only one answer possible --> stop iteration after 1st answer is found

found = False
string_1, line_1 = None, None
string_2, line_2 = None, None
answer = None

for i in range(len(lines)):
    string_1 = lines[i]
    for j in range(i + 1, len(lines)):
        string_2 = lines[j]
        for index in range(len(string_1)):
            if string_1[index] != string_2[index]:
                # First difference found --> compare end part of string
                if string_1[index + 1:] == string_2[index + 1:]:
                    found = True
                    answer = string_1[:index] + string_1[index + 1:]
                    line_1 = i
                    line_2 = j
                # If next part is not equal more differences occur --> continue with next line
                else:
                    break
        if found:
            break
    if found:
        break

print(f'\n---Part 2---\n')
print(f'Found word 1 to be --> {string_1} at line {line_1}')
print(f'Found word 2 to be --> {string_2} at line {line_2}')
print(f'\nThe answer to Part 2 is {answer}')
