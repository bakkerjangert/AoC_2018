players = 441
last_marble = 71032

multiple = 23

# Dict for scores
scores = {}
for i in range(players):
    scores[i + 1] = 0

print(scores)
# Init setup
table = {0: 0}
temp_table = {}
current_pos = 0

marble = 0
player = 1
# start play

while marble <= last_marble:
    marble += 1
    if len(table) == 1:  # Initiate first move
        table[1] = marble
        player += 1
        current_pos = 1
        continue
    if marble % 23 != 0:
        if current_pos + 1 == len(table):
            temp_table.clear
            for k, v in table.items():
                if k == 0:
                    temp_table[k] = v
                else:
                    temp_table[k + 1] = v
            temp_table[1] = marble
            table = temp_table.copy()
            current_pos = 1
        elif current_pos + 2 == len(table):
            table[current_pos + 2] = marble
            current_pos = len(table) - 1
        else:
            temp_table.clear()
            for k, v in table.items():
                if k < current_pos + 2:
                    temp_table[k] = v
                else:
                    temp_table[k + 1] = v
            temp_table[current_pos + 2] = marble
            table = temp_table.copy()
            current_pos += 2
    else:
        scores[player] = scores[player] + marble
        if current_pos > 6:
            current_pos -= 6
        else:
            current_pos = current_pos + len(table) - 6
        scores[player] = scores[player] + table[current_pos - 1]
        temp_table.clear()
        for k, v in table.items():
            if k < current_pos - 1:
                temp_table[k] = v
            elif k > current_pos - 1:
                temp_table[k - 1] = v
        table = temp_table.copy()
        current_pos -= 1
    if player == players:
        player = 1
    else:
        player += 1
    if marble % 1000 == 0:
        print('Processing marble', marble)
answer = 0
for k, v in scores.items():
    if v > answer:
        answer = v

print(answer)




