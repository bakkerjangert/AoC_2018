with open('input.txt') as f:
    lines = f.read().splitlines()

nano_bots = []
ranges = []

for i in range(len(lines)):
    nano_bots.append([])

    temp = lines[i].split('=<')[1]
    nano_bots[i].append(int(temp.split(',')[0]))
    nano_bots[i].append(int(temp.split(',')[1]))
    temp = temp.split('>')[0]
    nano_bots[i].append(int(temp.split(',')[2]))
    nano_bots[i].append(int(lines[i].split('r=')[-1]))
    ranges.append(int(lines[i].split('r=')[-1]))

range_bot = 0

print('Total of bots is', len(nano_bots))

for i in range(len(nano_bots)):
    if range_bot <= nano_bots[i][3]:
        range_bot = nano_bots[i][3]
        index = i


print('Range of largest bot is', range_bot, 'is', max(ranges), '. Minimum is', min(ranges))
print('Specific bot', nano_bots[index])

x_max = nano_bots[index][0]
y_max = nano_bots[index][1]
z_max = nano_bots[index][2]

# Set max nano bot to x = 0, y = 0, z = 0

for i in range(len(nano_bots)):
    nano_bots[i][0] -= x_max
    nano_bots[i][1] -= y_max
    nano_bots[i][2] -= z_max

print('Specific bot', nano_bots[index])

in_range = 0

for i in range(len(nano_bots)):
    if abs(nano_bots[i][0]) + abs(nano_bots[i][1]) + abs(nano_bots[i][2]) <= range_bot:
        in_range += 1

print('The answer is', in_range)
