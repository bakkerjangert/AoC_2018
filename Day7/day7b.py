import string

with open('input.txt') as f:
    lines = f.read().splitlines()

to_start = []
finished = []

for line in lines:
    to_start.append(line[-12])
    finished.append(line[5])

start_value = []
finish_value = []
for i in range(len(to_start)):
    if finished[i] not in to_start and finished[i] not in start_value:
        start_value.append(finished[i])
    if to_start[i] not in finished and to_start[i] not in finish_value:
        finish_value.append(to_start[i])

print('The start values are', start_value)
print('The end values are', finish_value)

dict_dependence = {}  # Count the number of dependants

for char in to_start:
    if char not in dict_dependence:
        dict_dependence[char] = 1
    else:
        dict_dependence[char] += 1

workers = 5
worker_time = []
for i in range(workers):
    worker_time.append(0)

time_table = {}
init_time = 60
for char in string.ascii_uppercase[0:26]:
    init_time += 1
    time_table[char] = init_time

possible_values = []
answer = []

for item in start_value:
    possible_values.append(item)

remaining_time = {}
next_value = []
timer = 0

temp_storage = []

while finish_value not in answer:
    possible_values.sort()
    print('-' * 10)
    print('The current workload is', worker_time)
    print('Workers working on', remaining_time)
    print('Posibilties are', possible_values)
    next_value.clear()
    for item in possible_values:
        for i in range(len(worker_time)):
            if worker_time[i] == 0:
                worker_time[i] = time_table[item]
                remaining_time[item] = time_table[item]
                temp_storage.append(item)
                break
    for item in temp_storage:
        possible_values.remove(item)
    temp_storage.clear()
    for i in range(len(worker_time)):
        if worker_time[i] != 0:
            worker_time[i] -= 1
    for k, v in remaining_time.items():
        if remaining_time[k] != 0:
            remaining_time[k] -= 1
        if remaining_time[k] == 0:
            answer.append(k)
            next_value.append(k)
            temp_storage.append(k)
    for item in temp_storage:
        del remaining_time[item]
    temp_storage.clear()
    for i in range(len(to_start)):
        for j in next_value:
            if finished[i] == j:
                dict_dependence[to_start[i]] -= 1
    for k, v in dict_dependence.items():
        if v == 0:
            possible_values.append(k)
            dict_dependence[k] -= 1
    timer += 1
    if dict_dependence[finish_value[0]] == -1:
        break

print('The answer is', timer + time_table[finish_value[0]])
answer.append(finish_value[0])
print('-' * 10)
for char in answer:
    print(char, end='')
print('')

