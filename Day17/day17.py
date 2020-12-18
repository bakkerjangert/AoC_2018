with open('input.txt') as f:
    lines = f.read().splitlines()

coordinates = []

for i in range(len(lines)):
    coordinates.append([])
    coordinates[i].append(lines[i][0])
    temp = lines[i].split('=')[1]
    coordinates[i].append(int(temp.split(',')[0]))
    temp = lines[i].split('..')[0]
    coordinates[i].append(int(temp.split('=')[-1]))
    coordinates[i].append(int(lines[i].split('..')[-1]))

# Determine x and y ranges

x_max = 0
first_x = True
y_max = 0
first_y = True

for line in coordinates:
    if line[0] == 'x':
        if line[1] > x_max:
            x_max = line[1]
        if first_x or line[1] < x_min:
            x_min = line[1]
            first_x = False
        if line[3] > y_max:
            y_max = line[3]
        if first_y or line[2] < y_min:
            y_min = line[2]
            first_y = False

    elif line[0] == 'y':
        if line[1] > y_max:
            y_max = line[1]
        if line[3] > x_max:
            x_max = line[3]
        if first_x or line[2] < x_min:
            x_min = line[2]
            first_x = False
        if first_y or line[1] < y_min:
            y_min = line[1]
            first_y = False

# Set x-boundary for 1 dot, except for y_max

x_min -= 2
x_max += 2
y_min -= 1
y_max += 1

# Rewrite data to start at x(0) is x_min

for line in coordinates:
    if line[0] == 'x':
        line[1] = line[1] - x_min
        line[2] = line[2] - y_min
        line[3] = line[3] - y_min
    elif line[0] == 'y':
        line[1] = line[1] - y_min
        line[2] = line[2] - x_min
        line[3] = line[3] - x_min

### Test if modification is correct

first_x = True
x_min_test = 0
x_max_test = 0
first_y = True
y_min_test = 0
y_max_test = 0

for line in coordinates:
    if line[0] == 'x':
        if x_max_test < line[1]:
            x_max_test = line[1]
        if first_x or x_min_test > line[1]:
            x_min_test = line[1]
            first_x = False
        if y_max_test < line[3]:
            y_max_test = line[3]
        if first_y or y_min_test > line[2]:
            y_min_test = line[2]
            first_y = False
    elif line[0] == 'y':
        if y_max_test < line[1]:
            y_max_test = line[1]
        if x_max_test < line[3]:
            x_max_test = line[3]
        if first_x or x_min_test > line[2]:
            x_min_test = line[2]
            first_x = False
        if first_y or y_min_test > line[1]:
            y_min_test = line[1]
            first_y = False

for line in coordinates:
    print(line)

print('x van', x_min, x_max, 'y van', y_min, y_max)
print('range x = 0', x_max - x_min, 'range y = 0', y_max - y_min)
print(x_min_test, x_max_test, y_max_test)

grid = []

for y in range(y_max - y_min + 1):
    grid.append([])
    for x in range(x_max - x_min + 1):
        grid[y].append('.')

grid[0][500 - x_min] = '+'

for i in range(len(coordinates)):
    if coordinates[i][0] == 'x':
        for j in range(coordinates[i][2], coordinates[i][3] + 1):
            grid[j][coordinates[i][1]] = '#'
    if coordinates[i][0] == 'y':
        for j in range(coordinates[i][2], coordinates[i][3] + 1):
            grid[coordinates[i][1]][j] = '#'


current_x = 500 - x_min
current_y = 1
stored_branches = []

counter = 0

while True:
    counter += 1
    if current_y == y_max - y_min:
        grid[current_y][current_x] = '|'
        if len(stored_branches) == 0:
            break
        current_x = stored_branches[-1][0]
        current_y = stored_branches[-1][1]
        del stored_branches[-1]
        continue
    # if counter > 7000:
    #     break
    if grid[current_y + 1][current_x] == '.':
        grid[current_y][current_x] = '|'
        current_y += 1
        continue
    if grid[current_y + 1][current_x] == '|':
        grid[current_y][current_x] = '|'
        if len(stored_branches) == 0:
            break
        current_x = stored_branches[-1][0]
        current_y = stored_branches[-1][1]
        del stored_branches[-1]
        continue
    if grid[current_y][current_x + 1] == '.' or grid[current_y][current_x - 1] == '.':
        x_plus = current_x
        x_minus = current_x
        checks = ['#']
        # checks = ['#', '|']
        while grid[current_y][x_plus] not in checks:
            x_plus += 1
            if x_plus == len(grid[0]) - 1:
                break
        while grid[current_y][x_minus] not in checks:
            x_minus -= 1
            if x_minus == 0:
                break
        x_plus_1 = current_x
        x_minus_1 = current_x
        checks_1 = ['.', '|']
        while grid[current_y + 1][x_plus_1] not in checks_1:
            x_plus_1 += 1
            if x_plus_1 == len(grid[0]) - 1:
                break
        while grid[current_y + 1][x_minus_1] not in checks_1:
            x_minus_1 -= 1
            if x_minus_1 == 0:
                break

        print('current coords =', current_x, current_y)
        print('boundary at y =', x_minus, x_plus)
        print('boundary at y + 1 =', x_minus_1, x_plus_1)
        print('-' * 10)

        # Fill depending on current y and y + 1 line

        if x_minus > x_minus_1 and x_plus < x_plus_1:  # Fill line with still water
            for x in range(x_minus + 1, x_plus):
                grid[current_y][x] = '~'
            current_y -= 1
            grid[current_y][current_x] = '.'
            continue
        if x_minus < x_minus_1 and x_plus > x_plus_1:  # Flow on both sides
            for x in range(x_minus_1, x_plus_1 + 1):
                grid[current_y][x] = '|'
            stored_branches.append([x_minus_1, current_y])
            current_x = x_plus_1
            continue
        if x_minus > x_minus_1 and x_plus > x_plus_1: # Flow on right side
            for x in range(x_minus + 1, x_plus_1 + 1):
                grid[current_y][x] = '|'
            current_x = x_plus_1
            continue
        if x_minus < x_minus_1 and x_plus < x_plus_1: # Flow on left side
            for x in range(x_minus_1, x_plus):
                grid[current_y][x] = '|'
            current_x = x_minus_1
            continue
    if grid[current_y][current_x - 1] == '#' and grid[current_y][current_x + 1] == '#':
        grid[current_y][current_x] = '~'
        current_y -= 1
        continue

    else:
        if len(stored_branches) > 0:
            current_x = stored_branches[-1][0]
            current_y = stored_branches[-1][1]
            del stored_branches[-1]
            continue
        elif len(stored_branches) == 0:
            break

for line in grid:
    for char in line:
        print(char, end='')
    print('')

# Count for answer

del grid[-1]

answer = 0
answer_2 = 0
water = ['|', '~']
still_water = ['~']
for line in grid:
    for char in line:
        if char in water:
            answer += 1
        if char in still_water:
            answer_2 += 1

print('The answer to part 1 is', answer)
print('The answer to part 2 is', answer_2)

for line in stored_branches:
    print(line)