with open('input.txt') as f:
    lines = f.read().splitlines()

#  lines = ['dabAcCaCBAcCcaDA']

original = lines[0]
upper_case = original.upper()

print('Length of string =', len(original))

positions = []
delete_no = []
iter = 0

while True:
    len_start = len(original)
    positions.clear()
    delete_no.clear()
    if len(original) < 2:
        break
    for num in range(len(original)-1):
        if original[num] != original[num + 1] and upper_case[num] == upper_case[num + 1]:
            positions.append(num)  # Mind that triples are added!
    for num_2 in range(len(positions) - 1):
        if positions[num_2] == positions[num_2 + 1] - 1:
            delete_no.append(num_2)
    delete_no.reverse()
    for num_3 in delete_no:
        del positions[num_3]
    positions.reverse()
    for x in positions:
        if len(original) == 2:
            original = []
            upper_case = []
        elif len(original) - 1 == x:
            original = original[:-3]
            upper_case = upper_case[:-3]
        elif x == 0:
            original = original[2:]
            upper_case = upper_case[2:]
        else:
            print('delete number', x)
            print('-' * 10)
            print(original)
            original = original[:x] + original[x + 2:]
            upper_case = upper_case[:x] + upper_case[x + 2:]
            print('-' * 10)
            print(original)
            print('END')
    iter += 1
    print(original)
    print('Length of string =', len(original), 'after', iter, 'iterations')
    if len_start == len(original):
        break  # Break if no letters are deleted

print(original)
print(upper_case)
print(len(original))
