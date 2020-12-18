def set_zero(pos_x, pos_y):
    # Shifts the coordinates to start at 1,1 (leaving a row of dots at the edge
    min_x = min(pos_x)
    min_y = min(pos_y)
    for i in range(len(pos_x)):
        pos_x[i] += -min_x + 1
        pos_y[i] += -min_y + 1

with open('input.txt') as f:
    lines = f.read().splitlines()

pos_x = []
pos_y = []
vel_x = []
vel_y = []

for i in range(len(lines)):
    pos_x.append(lines[i].split('position=<')[1])
    pos_x[i] = int(pos_x[i].split(',')[0])
    pos_y.append(lines[i].split(', ')[1])
    pos_y[i] = int(pos_y[i].split('> ')[0])
    vel_x.append(lines[i].split('y=<')[1])
    vel_x[i] = int(vel_x[i].split(',')[0])
    vel_y.append(lines[i].split(', ')[-1])
    vel_y[i] = int(vel_y[i].split('>')[0])


width = max(pos_x) - min(pos_x)
height = max(pos_y) - min(pos_y)
min_vel_x = min(vel_x)
max_vel_x = max(vel_x)
min_vel_y = min(vel_y)
max_vel_y = max(vel_y)

print('The grid is', width, ' wide x', height, 'high')
print('velocity in x is', min_vel_x, 'to', max_vel_x)
print('velocity in y is', min_vel_y, 'to', max_vel_y)
print('There are a total of', len(pos_x), 'points')

grid_limit = int(0.5 * len(pos_x))  # Assume at least 2 points on 1 line; try grid at 0.5 points
steps_x = (width - grid_limit) / (max_vel_x - min_vel_x)
steps_y = (height - grid_limit) / (max_vel_y - min_vel_x)
steps = int(max(steps_x, steps_y))

print('Initiate with ', steps, 'steps to reduce grid size')

for i in range(len(pos_x)):
    pos_x[i] = pos_x[i] + steps * vel_x[i]
    pos_y[i] = pos_y[i] + steps * vel_y[i]

time = steps

grid = []
# Initiate loop from here
while True:
    width = max(pos_x) - min(pos_x) + 2
    height = max(pos_y) - min(pos_y) + 2
    print('-' * 3, 'CALCULATING', '-' * 3)
    print('The new grid is now', width, ' wide x', height, 'high')

    # while True:
    set_zero(pos_x, pos_y)

    print('x-coords are ', min(pos_x), '-->', max(pos_x))
    print('y-coords are ', min(pos_y), '-->', max(pos_y))

    # Create empty grid
    grid.clear()
    for y in range(height + 1):
        grid.append([])
        for x in range(width + 1):
            grid[y].append('.')
    # Fill grid
    for i in range(len(pos_x)):
        grid[pos_y[i]][pos_x[i]] = '#'
    for line in grid:
        print('')
        for char in line:
            print(char, end='')
    print('')
    print('The current grid is now', width, ' wide x', height, 'high')
    answer = input("Enter the amount of steps or 'x' to quit")
    if answer == 'x':
        print('The current message took', time, 'seconds to appear')
        quit()
    for i in range(len(pos_x)):
        pos_x[i] = pos_x[i] + int(answer) * vel_x[i]
        pos_y[i] = pos_y[i] + int(answer) * vel_y[i]
    time = time + int(answer)


1
