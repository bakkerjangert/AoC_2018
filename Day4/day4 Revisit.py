# Advent of Code 2018 - Day 3
# Part 1
import re
import numpy as np


def most_sleepy_minute(guard_data):
    list_of_patrols = []
    for patrol in guard_data:
        list_of_patrols.append(list(patrol))
    sleepy_minute = None
    minutes = -999
    sleep_data = np.array(list_of_patrols)
    for minute_index in range(sleep_data.shape[1]):
        cur_minutes = list(sleep_data[:, minute_index]).count('#')
        if cur_minutes > minutes:
            sleepy_minute = minute_index
            minutes = cur_minutes
    return sleepy_minute, minutes


with open('input.txt') as f:
    lines = f.read().splitlines()

# Sort the input to date; luckily the string starts with the date so simple sort() functions does it
lines.sort()

# Generate sleeping data for each guard for each day --> similar to puzzle explanation ...##...#....#####..
# Start with empty string of 60 minutes awake (60 x '.')
# Adjust sleeping minutes with '#'
guards = {}
ID = None
awake = None
asleep = None
minutes_asleep = '.' * 60

for line in lines:
    if '#' in line:
        ID = int(re.search(r'#(.*?) ', line).group(1))
        if ID not in guards.keys():
            guards[ID] = [minutes_asleep]
        else:
            guards[ID].append(minutes_asleep)
    elif 'asleep' in line:
        asleep = int(line[15:17])
    elif 'wakes' in line:
        awake = int(line[15:17])
        # When guards awakes, add sleeping time to the data
        current_sleeping_time = guards[ID][-1]
        guards[ID][-1] = current_sleeping_time[:asleep] + '#' * (awake - asleep) + current_sleeping_time[awake:]

# Determine most sleepy guard
sleepy_ID = None
sleepy_time = 0

for guard in guards:
    current_sleep_time = 0
    for day in guards[guard]:
        current_sleep_time += day.count('#')
    if current_sleep_time > sleepy_time:
        sleepy_ID = guard
        sleepy_time = current_sleep_time

# Determine most sleepy minute
# Use numpy array to select columns easily

minute_1 = most_sleepy_minute(guards[sleepy_ID])[0]

print(f'\nThe answer to Part 1 = Guard {sleepy_ID} x minute {minute_1} = {sleepy_ID * minute_1}')

# Part 2
guard_ID_2 = None
minute_2 = None
no_of_minutes = -999

for guard in guards:
    data = most_sleepy_minute(guards[guard])
    if data[1] > no_of_minutes:
        guard_ID_2 = guard
        minute_2 = data[0]
        no_of_minutes = data[1]

print(f'\nThe answer to Part 2 = Guard {guard_ID_2} x minute {minute_2} = {guard_ID_2 * minute_2}')
