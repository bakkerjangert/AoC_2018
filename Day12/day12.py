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

cycle = 20
zero = 0

while cycle != 0:
    # Adjust current pattern to have .... at beginning and end
    for i in range(4):
        positions.insert(0, '.')
        positions.append('.')
        zero += 1

    previous = tuple(positions)
    # Reset string, Check wether needed?
    for k in range(len(positions)):
        positions[k] = '.'

    for i in range(2, len(positions) - 3):
        string = ''
        for j in range(i - 2, i + 3):
            string += previous[j]
        if string in patterns:
            positions[i] = outcomes[patterns.index(string)]
    cycle -= 1
    if cycle % 100 == 0:
        print('Currently at generation', cycle)

answer = 0
for i in range(len(positions)):
    if positions[i] == '#':
        answer += i - zero

print('Zero is', zero)
print(positions)
print('The answer is', answer)







