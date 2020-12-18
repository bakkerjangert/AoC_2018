def addr(before, instruct):
    before = before.copy()
    before[instruct[3]] = before[instruct[1]] + before[instruct[2]]
    return before


def addi(before, instruct):
    before = before.copy()
    before[instruct[3]] = before[instruct[1]] + instruct[2]
    return before


def mulr(before, instruct):
    before = before.copy()
    before[instruct[3]] = before[instruct[1]] * before[instruct[2]]
    return before


def muli(before, instruct):
    before = before.copy()
    before[instruct[3]] = before[instruct[1]] * instruct[2]
    return before


def banr(before, instruct):
    before = before.copy()
    before[instruct[3]] = before[instruct[1]] & before[instruct[2]]
    return before


def bani(before, instruct):
    before = before.copy()
    before[instruct[3]] = before[instruct[1]] & instruct[2]
    return before


def borr(before, instruct):
    before = before.copy()
    before[instruct[3]] = before[instruct[1]] | before[instruct[2]]
    return before


def bori(before, instruct):
    before = before.copy()
    before[instruct[3]] = before[instruct[1]] | instruct[2]
    return before


def setr(before, instruct):
    before = before.copy()
    before[instruct[3]] = before[instruct[1]]
    return before


def seti(before, instruct):
    before = before.copy()
    before[instruct[3]] = instruct[1]
    return before


def gtir(before, instruct):
    before = before.copy()
    if instruct[1] > before[instruct[2]]:
        before[instruct[3]] = 1
    else:
        before[instruct[3]] = 0
    return before


def gtri(before, instruct):
    before = before.copy()
    if before[instruct[1]] > instruct[2]:
        before[instruct[3]] = 1
    else:
        before[instruct[3]] = 0
    return before


def gtrr(before, instruct):
    before = before.copy()
    if before[instruct[1]] > before[instruct[2]]:
        before[instruct[3]] = 1
    else:
        before[instruct[3]] = 0
    return before


def eqir(before, instruct):
    before = before.copy()
    if instruct[1] == before[instruct[2]]:
        before[instruct[3]] = 1
    else:
        before[instruct[3]] = 0
    return before

def eqri(before, instruct):
    before = before.copy()
    if before[instruct[1]] == instruct[2]:
        before[instruct[3]] = 1
    else:
        before[instruct[3]] = 0
    return before


def eqrr(before, instruct):
    before = before.copy()
    if before[instruct[1]] == before[instruct[2]]:
        before[instruct[3]] = 1
    else:
        before[instruct[3]] = 0
    return before


with open('input.txt') as f:
    lines = f.read().splitlines()

before_org = []
instruct_org = []
after_org = []

for line in lines:
    if 'Before' in line:
        temp = line.split('[')[1]
        temp = temp.split(']')[0]
        before_org.append(temp.split(','))

    elif 'After' in line:
        temp = line.split('[')[1]
        temp = temp.split(']')[0]
        after_org.append(temp.split(','))

    elif len(line) >= 1 and line[-1].isdigit():
        instruct_org.append(line.split())

for i in before_org:
    for j in range(len(i)):
        i[j] = int(i[j])
for i in instruct_org:
    for j in range(len(i)):
        i[j] = int(i[j])
for i in after_org:
    for j in range(len(i)):
        i[j] = int(i[j])


dict_order = {}
temp = []

while len(dict_order) < 15:
    for i in range(len(before_org)):
        temp.clear()
        counter = 0
        if addr(before_org[i], instruct_org[i]) == after_org[i]:
            if 'adrr' not in dict_order.values():
                counter += 1
                temp.append('addr')
        if addi(before_org[i], instruct_org[i]) == after_org[i]:
            if 'adri' not in dict_order.values():
                counter += 1
                temp.append('addi')
        if mulr(before_org[i], instruct_org[i]) == after_org[i]:
            if 'mulr' not in dict_order.values():
                counter += 1
                temp.append('mulr')
        if muli(before_org[i], instruct_org[i]) == after_org[i]:
            if 'muli' not in dict_order.values():
                counter += 1
                temp.append('muli')
        if banr(before_org[i], instruct_org[i]) == after_org[i]:
            if 'banr' not in dict_order.values():
                counter += 1
                temp.append('banr')
        if bani(before_org[i], instruct_org[i]) == after_org[i]:
            if 'bani' not in dict_order.values():
                counter += 1
                temp.append('bani')
        if borr(before_org[i], instruct_org[i]) == after_org[i]:
            if 'borr' not in dict_order.values():
                counter += 1
                temp.append('borr')
        if bori(before_org[i], instruct_org[i]) == after_org[i]:
            if 'bori' not in dict_order.values():
                counter += 1
                temp.append('bori')
        if setr(before_org[i], instruct_org[i]) == after_org[i]:
            if 'setr' not in dict_order.values():
                counter += 1
                temp.append('setr')
        if seti(before_org[i], instruct_org[i]) == after_org[i]:
            if 'seti' not in dict_order.values():
                counter += 1
                temp.append('seti')
        if gtir(before_org[i], instruct_org[i]) == after_org[i]:
            if 'gtir' not in dict_order.values():
                counter += 1
                temp.append('gtir')
        if gtri(before_org[i], instruct_org[i]) == after_org[i]:
            if 'gtri' not in dict_order.values():
                counter += 1
                temp.append('gtri')
        if gtrr(before_org[i], instruct_org[i]) == after_org[i]:
            if 'gtrr' not in dict_order.values():
                counter += 1
                temp.append('gtrr')
        if eqir(before_org[i], instruct_org[i]) == after_org[i]:
            if 'eqir' not in dict_order.values():
                counter += 1
                temp.append('eqir')
        if eqri(before_org[i], instruct_org[i]) == after_org[i]:
            if 'eqri' not in dict_order.values():
                counter += 1
                temp.append('eqri')
        if eqrr(before_org[i], instruct_org[i]) == after_org[i]:
            if 'eqrr' not in dict_order.values():
                counter += 1
                temp.append('eqrr')
        if len(temp) == 1:
            dict_order[instruct_org[i][0]] = temp[0]

# Add last one manually

dict_order[0] = 'muli'

for i in range(16):
    print(i, dict_order[i])

with open('input_2.txt') as f:
    lines = f.read().splitlines()

inputs = []

for line in lines:
    inputs.append(line.split())


for i in inputs:
    for j in range(len(i)):
        i[j] = int(i[j])

current_pos = [0, 0, 0, 0]  # See middle of text to see the registers start at 0

for line in inputs:
    if dict_order[line[0]] == 'addr':
        current_pos = addr(current_pos, line)
    if dict_order[line[0]] == 'addi':
        current_pos = addi(current_pos, line)
    if dict_order[line[0]] == 'mulr':
        current_pos = mulr(current_pos, line)
    if dict_order[line[0]] == 'muli':
        current_pos = muli(current_pos, line)
    if dict_order[line[0]] == 'banr':
        current_pos = banr(current_pos, line)
    if dict_order[line[0]] == 'bani':
        current_pos = bani(current_pos, line)
    if dict_order[line[0]] == 'borr':
        current_pos = borr(current_pos, line)
    if dict_order[line[0]] == 'bori':
        current_pos = bori(current_pos, line)
    if dict_order[line[0]] == 'setr':
        current_pos = setr(current_pos, line)
    if dict_order[line[0]] == 'seti':
        current_pos = seti(current_pos, line)
    if dict_order[line[0]] == 'gtir':
        current_pos = gtir(current_pos, line)
    if dict_order[line[0]] == 'gtri':
        current_pos = gtri(current_pos, line)
    if dict_order[line[0]] == 'gtrr':
        current_pos = gtrr(current_pos, line)
    if dict_order[line[0]] == 'eqir':
        current_pos = eqir(current_pos, line)
    if dict_order[line[0]] == 'eqri':
        current_pos = eqri(current_pos, line)
    if dict_order[line[0]] == 'eqrr':
        current_pos = eqrr(current_pos, line)
    print('After applying', dict_order[line[0]], 'the current register is', current_pos)
    print('-' * 10)

print('The answer is', current_pos[0])
print(current_pos)
