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

ip_register = int(lines[0][-1])

del lines[0]

instruct = []

for i in range(len(lines)):
    instruct.append(lines[i].split())

for i in instruct:
    for j in range(len(i)):
        if j > 0:
            i[j] = int(i[j])

registers = [0, 0, 0, 0, 0, 0, 0]
ip_number = 0
counter = 0
while True:
    counter += 1
    if ip_number > len(instruct) - 1:
        break  # Program out of bound
    current_instruct = instruct[ip_number]
    registers[ip_register] = ip_number

    if current_instruct[0] == 'addr':
        registers = addr(registers, current_instruct)
    if current_instruct[0] == 'addi':
        registers = addi(registers, current_instruct)
    if current_instruct[0] == 'mulr':
        registers = mulr(registers, current_instruct)
    if current_instruct[0] == 'muli':
        registers = muli(registers, current_instruct)
    if current_instruct[0] == 'banr':
        registers = banr(registers, current_instruct)
    if current_instruct[0] == 'bani':
        registers = bani(registers, current_instruct)
    if current_instruct[0] == 'borr':
        registers = borr(registers, current_instruct)
    if current_instruct[0] == 'bori':
        registers = bori(registers, current_instruct)
    if current_instruct[0] == 'setr':
        registers = setr(registers, current_instruct)
    if current_instruct[0] == 'seti':
        registers = seti(registers, current_instruct)
    if current_instruct[0] == 'gtir':
        registers = gtir(registers, current_instruct)
    if current_instruct[0] == 'gtri':
        registers = gtri(registers, current_instruct)
    if current_instruct[0] == 'gtrr':
        registers = gtrr(registers, current_instruct)
    if current_instruct[0] == 'eqir':
        registers = eqir(registers, current_instruct)
    if current_instruct[0] == 'eqri':
        registers = eqri(registers, current_instruct)
    if current_instruct[0] == 'eqrr':
        registers = eqrr(registers, current_instruct)
    ip_number = registers[ip_register]
    ip_number += 1

print('The answer is', registers[0])

