with open('input.txt') as f:
    lines = f.read().splitlines()

init_pos = lines[0].split(': ')[1]

positions = []
for char in init_pos:
    positions.append(char)

patterns = []
outcomes = []
for line in range(2, len(lines)):
    patterns.append(lines[line].split(' => ')[0])
    outcomes.append(lines[line].split(' => ')[1])

answer_list = []
difference = []

# Only check for new plants; adjust patterns and outcome

length = len(patterns)

for i in range(length - 1, -1, -1):
    if outcomes[i] == '.':
        del outcomes[i]
        del patterns[i]

cycle = 200
zero = 0
last_init = ''
while cycle != 0:
    # Adjust current pattern to have ... at beginning and end
    counter = 0
    while char in init_pos == '.':
        counter += 1
    if counter < 4:
        init_pos = '.' * (4 - counter) + init_pos
        zero = zero + (4 - counter)
    if counter > 4:
        init_pos = init_pos[counter - 4:]
        zero = zero - (counter - 4)
    counter = 0
    while char in reversed(init_pos) == '.':
        counter += 1
    if counter < 4:
        init_pos = init_pos + '.' * (4 - counter)
    if counter > 4:
        init_pos = init_pos[:counter - 4]

    # previous = tuple(positions)
    # # Reset string, Check wether needed?
    # for k in range(len(positions)):
    #     positions[k] = '.'
    new_empty_string = '.' * len(init_pos)
    for i in range(2, len(init_pos) - 3):
        string = ''
        for j in range(i - 2, i + 3):
            string += init_pos[j]
        if string in patterns:
            new_empty_string = new_empty_string[:i] + '#' + new_empty_string[i + 1:]
            # positions[i] = outcomes[patterns.index(string)]
    cycle -= 1
    init_pos = new_empty_string
    if cycle % 100 == 0:
        print('Currently at generation', cycle)

    answer = 0
    for i in range(len(init_pos)):
        if init_pos[i] == '#':
            answer += i - zero
    answer_list.append(answer)

    if len(answer_list) > 1:
        difference.append(answer_list[-1] - answer_list[-2])
    print(answer_list)
    print(difference)

answer = 0
for i in range(len(init_pos)):
    if init_pos[i] == '#':
        answer += i - zero

print('Zero is', zero)
print(positions)
print('The answer is', answer)

print('Steady state found manually after 200 cycles, evey cycle increase is', difference[-1])

cycles = 50000000000

answer = answer + difference[-1] * (cycles - 200)

print('The answer to part 2 is', answer)





