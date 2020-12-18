from copy import deepcopy
with open('input.txt') as f:
    lines = f.read().splitlines()

def print_grid(end=False):
    print(f'\n--- Printing map ---')
    for line in grid:
        print('')
        for char in line:
            print(char, end='')
    print('')


def north():
    grid[pos[1] - 1][pos[0]] = '-'
    if pos[1] == 1:
        grid.insert(0, [])
        grid.insert(0, [])
        for j in range(len(grid[-1]) // 2):
            grid[0].append('#')
            grid[0].append('?')
            grid[1].append('?')
            grid[1].append('.')
        grid[0].append('#')
        grid[1].append('?')
        origin[1] += 2
        for branch in branches:
            branch[1] += 2
    else:
        pos[1] -= 2


def east():
    grid[pos[1]][pos[0] + 1] = '|'
    if pos[0] + 2 == len(grid[0]):
        for j in range(len(grid)):
            if j % 2 == 0:
                grid[j].append('?')
                grid[j].append('#')
            else:
                grid[j].append('.')
                grid[j].append('?')
    pos[0] += 2


def south():
    grid[pos[1] + 1][pos[0]] = '-'
    if pos[1] + 2 == len(grid):
        grid.append([])
        grid.append([])
        for j in range(len(grid[0]) // 2):
            grid[-1].append('#')
            grid[-1].append('?')
            grid[-2].append('?')
            grid[-2].append('.')
        grid[-1].append('#')
        grid[-2].append('?')
    pos[1] += 2


def west():
    grid[pos[1]][pos[0] - 1] = '|'
    if pos[0] == 1:
        for j in range(len(grid)):
            if j % 2 == 0:
                grid[j].insert(0, '?')
                grid[j].insert(0, '#')
            else:
                grid[j].insert(0, '.')
                grid[j].insert(0, '?')
        origin[0] += 2
        for branch in branches:
            branch[0] += 2
    else:
        pos[0] -= 2


print('There are', lines[0].count('|'), 'intersections')  # Wrong --> some are triple intersections!
print('There are', lines[0].count('('), 'intersections')  # Correct
print('There are', lines[0].count(')'), 'intersections')

route = lines[0][1:-1]

# ( = open new branch, add to route
# | = end of 1st or 2nd branch; backtrack opening point and continue
# |) = looping in first branch --> half length to be added
# ) = end of 2nd branch --> backtrack tp latest opening branch (

# append items to provide a backtrack to last opened branch (
# append [char, char_pos, current_len]

grid = [['#', '?', '#'],
        ['?', 'S', '?'],
        ['#', '?', '#']]

# route = 'WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))'

pos = [1, 1]
origin = [1, 1]
branches = []
for i in range(len(route)):
    val = route[i]
    if val == 'N':
        north()
    if val == 'S':
        south()
    if val == 'E':
        east()
    if val == 'W':
        west()
    if val == '(':
        branches.append(pos.copy())
    if val == '|':
        pos = branches[-1].copy()
    if val == ')':
        del branches[-1]

print_grid()
open_spaces = 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '?':
            grid[y][x] = '#'
        if grid[y][x] == '.':
            if grid[y-1][x] != '-' and grid[y+1][x] != '-' and grid[y][x-1] != '|' and grid[y][x+1] != '|':
                grid[y][x] = '#'
            else:
                open_spaces += 1
length = 0
change = False
print(f'open spaces = {open_spaces}')

while open_spaces != 0:
    change = False
    org_grid = deepcopy(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if org_grid[y][x] == 'S':
                if grid[y-1][x] == '-' and org_grid[y-2][x] == '.':
                    grid[y-2][x] = 'S'
                    open_spaces -= 1
                    change = True
                if grid[y+1][x] == '-' and org_grid[y+2][x] == '.':
                    grid[y+2][x] = 'S'
                    open_spaces -= 1
                    change = True
                if grid[y][x-1] == '|' and org_grid[y][x-2] == '.':
                    grid[y][x-2] = 'S'
                    open_spaces -= 1
                    change = True
                if grid[y][x+1] == '|' and org_grid[y][x+2] == '.':
                    grid[y][x+2] = 'S'
                    open_spaces -= 1
                    change = True
    if change:
        length += 1
        # print_grid()
        print(f'\nOpen spaces = {open_spaces}')

print_grid()
print(f'The answer is {length}')

print(len(route))
