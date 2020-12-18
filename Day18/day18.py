with open('input.txt') as f:
    lines = f.read().splitlines()

grid = []

for i in range(len(lines)):
    grid.append([])
    for j in range(len(lines[i])):
        grid[i].append(lines[i][j])

minutes = 10

grid_update = []

for y in range(len(grid)):
    grid_update.append([])
    for x in range(len(grid[y])):
        grid_update[y].append(grid[y][x])



print('-' * 10)
print('The initial grid looks like this')
print('-' * 10)

for line in grid_update:
    for char in line:
        print(char, end='')
    print('')

for i in range(minutes):
    for y in range(len(grid)):
        for x in range(len(grid[y])):

            x_start = max(0, x - 1)
            x_end = min(len(grid[y]) - 1, x + 1)
            y_start = max(0, y - 1)
            y_end = min(len(grid) - 1, y + 1)
            # print('Current x-y', x, y)
            # print('x-range', x_start, x_end)
            # print('y_range', y_start, y_end)
            if grid[y][x] == '.':
                count = 0
                for y_1 in range(y_start, y_end + 1):
                    for x_1 in range(x_start, x_end + 1):
                        if grid[y_1][x_1] == '|':
                            if not(y == y_1 and x == x_1):
                                count += 1
                if count >= 3:
                    grid_update[y][x] = '|'

            if grid[y][x] == '|':
                count = 0
                for y_1 in range(y_start, y_end + 1):
                    for x_1 in range(x_start, x_end + 1):
                        if grid[y_1][x_1] == '#':
                            if not (y == y_1 and x == x_1):
                                count += 1
                if count >= 3:
                    grid_update[y][x] = '#'

            if grid[y][x] == '#':
                count_tree = 0
                count_yard = 0
                for y_1 in range(y_start, y_end + 1):
                    for x_1 in range(x_start, x_end + 1):
                        if grid[y_1][x_1] == '|':
                            if not(y == y_1 and x == x_1):
                                count_tree += 1
                        if grid[y_1][x_1] == '#':
                            if not(y == y_1 and x == x_1):
                                count_yard += 1
                if not (count_tree >= 1 and count_yard >= 1):
                    grid_update[y][x] = '.'
    print('-' * 10)
    print('After', i + 1, 'minutes the grid looks like this')
    print('-' * 10)

    for line in grid_update:
        for char in line:
            print(char, end='')
        print('')

    grid.clear()
    for y in range(len(grid_update)):
        grid.append([])
        for x in range(len(grid_update[y])):
            grid[y].append(grid_update[y][x])


count_tree = 0
count_yard = 0

for line in grid:
    for char in line:
        if char == '|':
            count_tree += 1
        if char == '#':
            count_yard += 1

print('The answer is', count_tree * count_yard)