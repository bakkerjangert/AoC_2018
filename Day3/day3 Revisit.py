# Advent of Code 2018 - Day 3 Part 1 and 2
import re
with open('input.txt') as f:
    lines = f.read().splitlines()


class Claim(object):
    def __init__(self, string):
        self.ID = int(re.search(r'#(.*?) @', string).group(1))
        self.x_start = int(re.search(r'@ (.*?),', string).group(1))
        self.y_start = int(re.search(r',(.*?):', string).group(1))
        self.x_end = self.x_start + int(re.search(r': (.*?)x', string).group(1))
        self.y_end = self.y_start + int(string.split('x')[-1])


# Part 1
# Set up instruction instance per line
instructions = []
for line in lines:
    instructions.append(Claim(line))

# Setup initial unclaimed fabric
fabric = []
width = 1000  # Puzzle input
height = 1000  # Puzzle input
for y in range(width):
    fabric.append([])
    for x in range(height):
        fabric[-1].append('.')

# Filling the grid with Claims and check multiple spaces
# --> '.' = Unclaimed fabric
# --> '#' = Claimed by a single Elf
# --> 'X' = Claimed by 2 or more Elf's
multiple_count = 0
for instruction in instructions:
    for x in range(instruction.x_start, instruction.x_end):
        for y in range(instruction.y_start, instruction.y_end):
            if fabric[y][x] == '.':
                fabric[y][x] = '#'
            elif fabric[y][x] == '#':
                fabric[y][x] = 'X'
                multiple_count += 1
            else:
                pass

print(f'\n--- Part 1 ---\n')
print(f'The answer to Part 1 = {multiple_count}')

# Part 2
answer_ID = None
found = False
for instruction in instructions:
    index_x_start = instruction.x_start
    index_x_end = instruction.x_end
    for y in range(instruction.y_start, instruction.y_end):
        # All entries shall be '#' if the fabric is the correct answer
        if fabric[y][index_x_start:index_x_end].count('#') != len(fabric[y][index_x_start:index_x_end]):
            break
        if y == instruction.y_end - 1:  # If all lines, up to the last one are all valid, answer is found
            found = True
    if found:
        answer_ID = instruction.ID
        break

print(f'\n--- Part 2 ---\n')
print(f'The answer to Part 2 = {answer_ID}')
