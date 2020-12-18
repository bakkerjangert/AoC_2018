with open('input.txt') as f:
    lines = f.read().splitlines()

string = lines[0].split(' ')
for i in range(len(string)):
    string[i] = int(string[i])

tracker = []
meta_data = []
level_meta = []
end_node = False
while len(string) > 0:
    if len(tracker) == 0:
        tracker.append(string[0])
        tracker.append(string[1])
        string = string[2:]
        level = 0
        level_meta.append([])
    child_node = tracker[-2]
    print('-' * 10)
    print(tracker)
    print(level_meta)
    print('Len meta_level =', len(level_meta), 'and level =', level)
    if child_node == 0: # Meta data
        if end_node:
            print('Node without Child found')
            # Node is has node child nodes; calculate meta data
            temp_sum = 0
            print('The value = ', end=' ')
            for i in range(tracker[-1]):
                print(string[i], end='+ ')
                temp_sum += string[i]
            print('')
            level_meta[level - 1].append(temp_sum)
            end_node = False
        else:
            # Node has Child nodes; determine meta with new rule
            temp_sum = 0
            print('The nodes are', end='')
            for i in range(tracker[-1]):
                print('', string[i], end=',')
                if string[i] <= len(level_meta[level]):
                    temp_sum += level_meta[level][string[i] - 1]
            print('Temp sum =', temp_sum)
            level_meta[level - 1].append(temp_sum)
        if level > 0:
            del level_meta[level]
        if level == 0:  # End of root node
            answer = 0
            for i in range(tracker[-1]):
                if string[i] <= len(level_meta[level]):
                    answer += level_meta[level][string[i] - 1]
        string = string[tracker[-1]:]
        del tracker[-1]  # Delete meta dat entry
        del tracker[-1]  # Delete 0 childhood number
        level -= 1
    else:  # Child_node present
        tracker[-2] = tracker[-2] - 1
        tracker.append(string[0])
        if string[0] == 0:
            end_node = True
        tracker.append(string[1])
        level_meta.append([])
        level += 1
        string = string[2:]

print('The answer is', answer)
