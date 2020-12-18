# Advent of Code 2018 - Day 3 part a

with open('input.txt') as f:
    lines = f.read().splitlines()

off_set = []
area = []
off_height = []
off_width = []
area_height = []
area_width = []
total_h = []
total_w = []
ID = []

for line in range(len(lines)):
    off_set.append(lines[line].split("@ ")[1])
    off_set[line] = off_set[line].split(": ")[0]
    area.append(lines[line].split(": ")[1])
    off_height.append(int(off_set[line].split(",")[0]))
    off_width.append(int(off_set[line].split(",")[1]))
    area_height.append(int(area[line].split("x")[0]))
    area_width.append(int(area[line].split("x")[1]))
    total_h.append(max(off_height)+max(area_height))
    total_w.append(max(off_width)+max(area_width))
    ID.append(lines[line].split(' @ ')[0])
    ID[line] = int(ID[line].split("#")[1])

total_height = max(total_h)
total_width = max(total_w)

grid = []
for i in range(total_height):
    grid.append([])
    for j in range(total_width):
        grid[i].append(0)

# for line in grid:
#     print(line)  # Empty grid with zero's

for i in range(len(off_height)):
    for x in range(off_width[i], off_width[i] + area_width[i]):
        for y in range(off_height[i], off_height[i] + area_height[i]):
            grid[y][x] = grid[y][x] + 1

doubles = 0

for i in range(total_height):
    for j in range(total_width):
        if grid[i][j] >= 2:
            doubles += 1

print('The answer is', doubles)

# Advent of Code 2018 - Day 3 part b

fini = False
row_break = False

for i in range(len(off_height)):
    if fini == True:
        break
    area_line = area_height[i] * area_width[i]
    area_count = 0
    for x in range(off_width[i], off_width[i] + area_width[i]):
        if row_break == True or fini == True:
            row_break = False
            break
        for y in range(off_height[i], off_height[i] + area_height[i]):
            area_count += 1
            if grid[y][x] != 1:
                row_break = True
                break
            if area_count == area_line:
                id_num = ID[i]
                fini = True

print('The answer is ID', id_num)


# To check print numbers of ID; all should be 1
print('-' *10)
print('To proof the numbers for the ID are printed:')
for x in range(off_width[id_num - 1], off_width[id_num - 1] + area_width[id_num - 1]):
    for y in range(off_height[id_num - 1], off_height[id_num - 1] + area_height[id_num - 1]):
        print(grid[y][x], end='')
    print('')
