with open('input.txt') as f:
    lines = f.read().splitlines()

x_coord = []
y_coord = []

for i in range(len(lines)):
    x_coord.append(int(lines[i].split(',')[0]))
    y_coord.append(int(lines[i].split(',')[1]))

#  Only need to make grid from x_min to x_max and y_min to y_max

x_min = min(x_coord)
y_min = min(y_coord)

for i in range(len(x_coord)):
    x_coord[i] -= x_min
    y_coord[i] -= y_min

x_max = max(x_coord)
y_max = max(y_coord)

chars = 'abcdefghjklmnopqrstuvwxyz'
chars = chars.lower() + chars.upper()

grid = []
for y in range(y_max):
    grid.append([])
    for x in range(x_max):
        grid[y].append('.')

print('The grid is', len(grid[0]), 'x', len(grid))

test_dict = {}
for char in chars:
    test_dict[char] = 0

for y in range(y_max):
    for x in range(x_max):
        i = 0
        for k,v in test_dict.items():
            test_dict[k] = abs(x_coord[i] - x) + abs(y_coord[i] - y)
            i += 1
        temp = 1000
        for k, v in test_dict.items():
            if v < temp:
                temp = v
                value = k
        counter = 0
        for k, v in test_dict.items():
            if v == temp:
                counter += 1
        if counter > 1:
            value = '-'
        grid[y][x] = value

for line in grid:
    print(line)

# Empty dict before counting
for char in chars:
    test_dict[char] = 0

for y in range(y_max):
    for x in range(x_max):
        if grid[y][x] == '-':
            continue
        if x == 0 or y == 0 or x == x_max - 1 or y == y_max - 1:
            test_dict[grid[y][x]] -= 50000 # Goes to infinite
        else:
            test_dict[grid[y][x]] += 1

values = []
for k, v in test_dict.items():
    print(k, v)
    values.append(v)

print('The answer is', max(values))

# Part b

distance = 10000

x_max = x_max + 2 * int((distance / len(chars)))
y_max = y_max + 2 * int((distance / len(chars)))

for i in range(len(chars)):
    x_coord[i] += distance / len(chars)
    y_coord[i] += distance / len(chars)

grid_2 = []

for y in range(y_max):
    grid_2.append([])
    for x in range(x_max):
        grid_2[y].append('.')

answer = 0
for y in range(int(y_max)):
    for x in range(int(x_max)):
        counter = 0
        for i in range(len(x_coord)):
            counter += abs(x - x_coord[i]) + abs(y - y_coord[i])
        if counter < distance:
            grid_2[y][x] = '#'
            answer += 1

for line in grid_2:
    print(line)
print('The answer =', answer)
