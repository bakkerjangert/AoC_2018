with open('input.txt') as f:
    lines = f.read().splitlines()

string = lines[0].split(' ')
for i in range(len(string)):
    string[i] = int(string[i])

tracker = []
meta_data = []
count = 1
while len(string) > 0:
    if len(tracker) == 0:
        tracker.append(string[0])
        tracker.append(string[1])
        string = string[2:]
    child_node = tracker[-2]
    if len(tracker) == 0:
        count += 1
    print('-' * 10)
    print(tracker)
    if child_node == 0: # Meta data
        for i in range(tracker[-1]):
            meta_data.append(string[i])
        string = string[tracker[-1]:]
        del tracker[-1]  # Delete meta dat entry
        del tracker[-1]  # Delete 0 childhood number
    else:  # Child_node present
        tracker[-2] = tracker[-2] - 1
        tracker.append(string[0])
        tracker.append(string[1])
        string = string[2:]

answer = 0
print('There are', count, 'root nodes')
print(sum(meta_data))
for item in meta_data:
    answer = answer + item

print('The answer is', answer)
