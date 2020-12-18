def calc_power(x, y, serial):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial
    power_level = power_level * rack_id
    if len(str(power_level)) > 2:
        power_level = int(str(power_level)[-3])
    else:
        power_level = 0
    power_level -= 5

    return power_level


serial_number = 5034  # Puzzle input

grid = []
for y in range(300):
    grid.append([])
    for x in range(300):
        grid[y].append(calc_power(x + 1, y + 1, serial_number))

for line in grid:
    print(line)

x_y = [0, 0]
checker = 0
for y in range(300 - 3):
    for x in range(300 - 3):
        temp_sum = 0
        for d_y in range(3):
            for d_x in range(3):
                temp_sum += grid[y + d_y][x + d_x]
        if temp_sum > checker:
            checker = temp_sum
            x_y[0] = x + 1
            x_y[1] = y + 1

print('The answer to part 1 =', x_y)

sum_table = []
for y in range(len(grid)):
    sum_table.append([])
    for x in range(len(grid[y])):
        temp_sum = 0
        if x != 0:
            temp_sum += sum_table[y][x - 1]
        if y != 0:
            temp_sum += sum_table[y - 1][x]
        if y == 0 or x == 0:
            sum_table[y].append(grid[y][x] + temp_sum)
        else:
            sum_table[y].append(grid[y][x] + sum(grid[y][0: x]) + sum_table[y - 1][x])

x_y_z = [0, 0, 0]
checker = 0
rows = len(grid)
for i in range(1, 301):
    print('-' * 10)
    print('Checking size', i, 'x', i)
    for y in range(rows - i):
        for x in range(rows - i):
            if x == 0 and y == 0:
                top_left = 0
                top_right = 0
                bot_left = 0
                bot_right = sum_table[y + (i-1)][x + (i-1)]
            elif x == 0:
                top_left = 0
                top_right = sum_table[y - 1][x + (i-1)]
                bot_left = 0
                bot_right = sum_table[y + (i - 1)][x + (i - 1)]
            elif y == 0:
                top_left = 0
                top_right = 0
                bot_left = sum_table[y + (i - 1)][x - 1]
                bot_right = sum_table[y + (i - 1)][x + (i - 1)]
            else:
                top_left = sum_table[y - 1][x - 1]
                top_right = sum_table[y - 1][x + (i - 1)]
                bot_left = sum_table[y + (i - 1)][x - 1]
                bot_right = sum_table[y + (i - 1)][x + (i - 1)]
            total = top_left + bot_right - top_right - bot_left
            if total > checker:
                checker = total
                x_y_z[0] = [x + 1]
                x_y_z[1] = [y + 1]
                x_y_z[2] = [i]

print(x_y_z)
