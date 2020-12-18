# Advent of Code 2018 - Day 2 part a

with open('input.txt') as f:
    lines = f.read().splitlines()

count_2 = 0
count_3 = 0
count_dict = {}

for line in lines:
    count_dict.clear()
    for letter in line:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    if 2 in count_dict.values():
        count_2 += 1
    if 3 in count_dict.values():
        count_3 += 1
print('The answer to Day 2 part a is', count_2 * count_3)

# Day 2 Part b

counter = 100
fini = False

print('Total lines =', len(lines))
for i in range(len(lines)):
    print('test line', i + 1)
    if fini == True:
         break
    for j in range(i + 1, len(lines)):
        print('---- with line', j + 1)
        if fini == True:
            break
        counter = 0
        for char in range(len(lines[i])):
            if fini == True:
                break
            if lines[i][char] != lines[j][char]:
                counter += 1
            # if counter > delta:
            #     break
            if counter <= 1 and char == len(lines[i]) - 1:
                word_1 = lines[i]
                word_2 = lines[j]
                fini = True

print(word_1)
print(word_2)
print('-' * 10)

answer = []
for char in range(len(word_1)):
    if word_1[char] == word_2[char]:
        answer.append(word_1[char])

print(''.join(answer))
