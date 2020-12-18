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

answer = 0
count_list = []
for i in range(len(before_org)):
    counter = 0
    if addr(before_org[i], instruct_org[i]) == after_org[i]:
        counter += 1
    if addi(before_org[i], instruct_org[i]) == after_org[i]:
        counter += 1
    if mulr(before_org[i], instruct_org[i]) == after_org[i]:
        counter += 1
    if muli(before_org[i], instruct_org[i]) == after_org[i]:
        counter += 1
    if banr(before_org[i], instruct_org[i]) == after_org[i]:
        counter += 1
    if bani(before_org[i], instruct_org[i]) == after_org[i]:
        counter += 1
    if borr(before_org[i], instruct_org[i]) == after_org[i]:
        counter += 1
    if bori(before_org[i], instruct_org[i]) == after_org[i]:
        counter += 1
    if setr(before_org[i], instruct_org[i]) == after_org[i]:
        counter += 1
    if seti(before_org[i], instruct_org[i]) == after_org[i]:
        counter += 1
    if gtir(before_org[i], instruct_org[i]) == after_org[i]:
        counter += 1
    if gtri(before_org[i], instruct_org[i]) == after_org[i]:
        counter += 1
    if gtrr(before_org[i], instruct_org[i]) == after_org[i]:
        counter += 1
    if eqir(before_org[i], instruct_org[i]) == after_org[i]:
        counter += 1
    if eqri(before_org[i], instruct_org[i]) == after_org[i]:
        counter += 1
    if eqrr(before_org[i], instruct_org[i]) == after_org[i]:
        counter += 1
    if counter >= 3:
        answer += 1
    count_list.append(counter)


print('The answer is', answer)



