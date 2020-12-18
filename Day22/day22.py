depth = 8103
target_x = 9
target_y = 758
modules = 20183

grid = []

for i in range(target_y + 1):
    grid.append([])
    for j in range(target_x + 1):
        grid[i].append('.')

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if x == 0 and y == 0:
            grid[y][x] = 0
        if x == target_x and y == target_y:
            grid[y][x] = 0
        elif y == 0:
            grid[y][x] = (x * 16807)
        elif x == 0:
            grid[y][x] = (y * 48271)
        else:
            grid[y][x] = ((grid[y][x - 1] + depth) % modules * (grid[y - 1][x] + depth) % modules) % modules


for y in range(len(grid)):
    for x in range(len(grid[y])):
        grid[y][x] = (grid[y][x] + depth) % modules
        print(x, y, (grid[y][x] + depth) % 3, end='; ')
        if grid[y][x] % 3 == 0:
            grid[y][x] = '.'
        elif grid[y][x] % 3 == 1:
            grid[y][x] = '='
        elif grid[y][x] % 3 == 2:
            grid[y][x] = '|'
    print('')

for y in range(len(grid)):
    for x in range(len(grid[y])):
        print(grid[y][x], end='')
    print('')

answer = 0

for line in grid:
    for char in line:
        if char == '.':
            answer += 0
        if char == '=':
            answer += 1
        if char == '|':
            answer += 2

print('The answer is', answer)

