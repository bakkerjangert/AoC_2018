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

possible_values = []
answer = []

for item in start_value:
    possible_values.append(item)


while finish_value not in answer:
    print('-' * 10)
    print('The current answer is', answer)
    print('Possible values are', possible_values)
    print('Dependecies are', dict_dependence)
    possible_values.sort()
    next_value = possible_values[0]
    answer.append(next_value)
    possible_values.remove(next_value)
    for i in range(len(to_start)):
        if finished[i] == next_value:
            dict_dependence[to_start[i]] -= 1
    for k, v in dict_dependence.items():
        if v == 0:
            possible_values.append(k)
            dict_dependence[k] -= 1
    if dict_dependence[finish_value[0]] == -1:
        break
answer.append(finish_value[0])
print('-' * 10)
for char in answer:
    print(char, end='')
print('')






