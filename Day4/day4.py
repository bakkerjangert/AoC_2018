# Advent of Code 2018 - Day 3 part a

with open('input.txt') as f:
    lines = f.read().splitlines()

lines.sort()

for line in (lines):
    print(line)
print('-' * 10)

guards = {}
guard_max_sleep = 0

for line in lines:
    if '#' in line:
        guard_id = line.partition('#')[2]
        guard_id_num = ''
        digit_id = False
        delta = 0
        while digit_id == False:
            if guard_id[delta].isdigit() == True:
                guard_id_num += guard_id[delta]
                delta += 1
            else:
                digit_id = True
        if guard_id_num not in guards:
            guards[guard_id_num] = 0
    if 'asleep' in line:
        sleep_1 = int(line[11:13])
        sleep = int(line[15:17])
    if 'wakes up' in line:
        awake = int(line[15:17])
        if sleep_1 == 0:
            guards[guard_id_num] += (awake - sleep)
        else:  # start at 00 minutes
            guards[guard_id_num] += (awake + (sleep - 60))

counter = 0
for k, v in guards.items():
    if v > counter:
        counter = v
        guard_id_num = k


for k, v in guards.items():
    print(k, v)


minutes = {}
for i in range(60):
    minutes[i] = 0


guard = False
for line in lines:
    if '#' in line:
        if guard_id_num in line:
            guard = True
        else:
            guard = False
    if 'asleep' in line:
        sleep = int(line[15:17])
    if 'wakes up' in line:
        awake = int(line[15:17])
        if guard == True:
            for k in range(sleep,awake):
                minutes[k] += 1
print(minutes)
counter = 0
for k, v in minutes.items():
    if v > counter:
        counter = v
        answer = k

print(guard_id_num)
print(answer)
print('The answer =', answer * int(guard_id_num))

# Part 4b

guards_2 = {}
for i in guards.keys():
    guards_2[i] = {}
    for j in range(60):
        guards_2[i][j] = 0



guard = False
for k, v in guards_2.items():
    for line in lines:
        if '#' in line:
            if k in line:
                guard = True
            else:
                guard = False
        if 'asleep' in line:
            sleep = int(line[15:17])
        if 'wakes up' in line:
            awake = int(line[15:17])
            if guard == True:
                for var in range(sleep,awake):
                    guards_2[k][var] += 1

for k, v in guards_2.items():
    print(k, v)

counter = 0
for k, v in guards_2.items():
    for i in range(60):
        if guards_2[k][i] > counter:
            counter = guards_2[k][i]
            guard_id_2 = int(k)
            minute = i
print(f'Guard ID = {guard_id_2}, minute = {minute}')
print('The answer to part b =', guard_id_2 * minute)
