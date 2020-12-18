import networkx as nx

depth = 8103
target_x = 9
target_y = 758
boundary_x = target_x + 100
boundary_y = target_y + 100
modules = 20183

grid = []

for i in range(boundary_y + 1):
    grid.append([])
    for j in range(boundary_x + 1):
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
        if grid[y][x] % 3 == 0:
            grid[y][x] = '.'
        elif grid[y][x] % 3 == 1:
            grid[y][x] = '='
        elif grid[y][x] % 3 == 2:
            grid[y][x] = '|'

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

# # # Make 3 maps for evey gear

torch_map = []

for y in range(len(grid)):
    torch_map.append([])
    for x in range(len(grid[y])):
        if grid[y][x] == '.' or grid[y][x] == '|':
            torch_map[y].append('.')
        else:
            torch_map[y].append('#')
torch_map[0][0] = 'M'
torch_map[target_y][target_x] = 'T'

print('-' * 15)
print('The torch map looks like this')
print('-' * 15)
for y in torch_map:
    for x in y:
        print(x, end=',')
    print('')

### Climb map

climb_map = []

for y in range(len(grid)):
    climb_map.append([])
    for x in range(len(grid[y])):
        if grid[y][x] == '.' or grid[y][x] == '=':
            climb_map[y].append('.')
        else:
            climb_map[y].append('@')

climb_map[0][0] = 'M'
climb_map[target_y][target_x] = 'T'

print('-' * 15)
print('The climb map looks like this')
print('-' * 15)

for y in climb_map:
    for x in y:
        print(x, end=',')
    print('')

### No gear map

no_gear_map = []

for y in range(len(grid)):
    no_gear_map.append([])
    for x in range(len(grid[y])):
        if grid[y][x] == '|' or grid[y][x] == '=':
            no_gear_map[y].append('.')
        else:
            no_gear_map[y].append('&')

no_gear_map[0][0] = 'M'
no_gear_map[target_y][target_x] = 'T'

print('-' * 15)
print('The No Gear map looks like this')
print('-' * 15)

for y in no_gear_map:
    for x in y:
        print(x, end=',')
    print('')

# Build networkx graph

G = nx.Graph()

# Torch_map at level z = 0
for y in range(len(torch_map)):
    for x in range(len(torch_map[0])):
        if torch_map[y][x] == '.':
            G.add_node((x, y, 0))
            G.add_node((0, 0, 0))
            G.add_node((target_x, target_y, 0))

# Climb_map at level z = 1
for y in range(len(climb_map)):
    for x in range(len(climb_map[0])):
        if climb_map[y][x] == '.':
            G.add_node((x, y, 1))
            G.add_node((0, 0, 1))
            G.add_node((target_x, target_y, 1))

# No gear map at level z = 2
for y in range(len(no_gear_map)):
    for x in range(len(no_gear_map[0])):
        if no_gear_map[y][x] == '.':
            G.add_node((x, y, 2))

# Add edges; between levels weight is 7; else weight is 1
for z in (0, 1, 2):
    for y in range(len(torch_map)):
        for x in range(len(torch_map[0])):
            if x != 0:
                if (x - 1, y, z) in G.nodes and (x, y, z) in G.nodes:
                    G.add_edge((x, y, z), (x - 1, y, z), weight=1.0)
            if x != len(torch_map[0]) - 1:
                if (x + 1, y, z) in G.nodes and (x, y, z) in G.nodes:
                    G.add_edge((x, y, z), (x + 1, y, z), weight=1.0)
            if y != 0:
                if (x, y - 1, z) in G.nodes and (x, y, z) in G.nodes:
                    G.add_edge((x, y, z), (x, y - 1, z), weight=1.0)
            if y != len(torch_map) - 1:
                if (x, y + 1, z) in G.nodes and (x, y, z) in G.nodes:
                    G.add_edge((x, y, z), (x, y + 1, z), weight=1.0)
            if z != 0:
                if (x, y, z - 1) in G.nodes and (x, y, z) in G.nodes:
                    G.add_edge((x, y, z), (x, y, z - 1), weight=7.0)
            else:
                if (x, y, 2) in G.nodes and (x, y, z) in G.nodes:
                    G.add_edge((x, y, z), (x, y, 2), weight=7.0)
            if z != 2:
                if (x, y, z + 1) in G.nodes and (x, y, z) in G.nodes:
                    G.add_edge((x, y, z), (x, y, z + 1), weight=7.0)
            else:
                if (x, y, 0) in G.nodes and (x, y, z) in G.nodes:
                    G.add_edge((x, y, z), (x, y, 0), weight=7.0)

start = (0, 0, 0)
end = (target_x, target_y, 0)

path = nx.dijkstra_path(G, start, end)
for item in path:
    print(item)

answer = 0
for i in range(len(path) - 1):
    if path[i][2] == path[i+1][2]:
        answer += 1
    else:
        answer += 7

print(f'The answer is {answer}')

