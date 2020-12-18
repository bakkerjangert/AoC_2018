players = 10
last_marble = 1618

multiple = 23

# Dict for scores
scores = {}
for i in range(players):
    scores[i + 1] = 0

# Init setup
table = []

current_pos = 0

marble = 0
player = 1
# start play
while marble <= last_marble:
    marble += 1
    if len(table) == 1:  # First deviating move
        table[1] = marble
        player += 1
        current_pos = 1
        continue
    if marble % 23 != 0:
        if current_pos + 1 == len(table):
            # Copy table
            for k in table.keys():
                if k > 0 and table == table_1:
                    table_2[k + 1] = v
                elif k > 0 and table == table_2:
                    table_1[k + 1] = v
                # Switch table
            if table == table_1:
                table = table_2
            else:
                table = table_1
            table[1] = marble
            current_pos = 1
        elif current_pos + 2 == len(table):
            table[len(table)] = marble
            current_pos = len(table) - 1
        else:
            # Copy table
            if table == table_1:
                table_2.clear()
                for k, v in table.items():
                    table_2[k] = v
            else:
                table_1.clear()
                for k, v in table.items():
                    table_1[k] = v

            for k in table.keys():
                if k > current_pos + 2 and table == table_1:
                    table_2[k + 1] = v
                elif k > current_pos + 2 and table == table_2:
                    table_1[k + 1] = v
            # Switch table --> 2nd time; make def
            if table == table_1:
                table = table_2
            else:
                table = table_1
            table[current_pos + 2] = marble
            current_pos += 2
    else:
        scores[player] = scores[player] + marble
        if current_pos > 6:
            current_pos -= 6
        else:
            current_pos = current_pos + len(table) - 6
        scores[player] = scores[player] + table[current_pos - 1]
        del table[current_pos - 1]

        # Copy table
        if table == table_1:
            table_2.clear()
            for k, v in table.items():
                table_2[k] = v
        else:
            table_1.clear()
            for k, v in table.items():
                table_1[k] = v

        for k in table.keys():
            if k > current_pos - 1 and table == table_1:
                table_2[k + 1] = table_2.pop(k)
            elif k > current_pos - 1 and table == table_2:
                table_1[k + 1] = table_1.pop(k)
        # Switch table --> 2nd time; make def
        if table == table_1:
            table = table_2
        else:
            table = table_1
        current_pos -= 1
    if player == players:
        player = 1
    else:
        player += 1

answer = 0
for k, v in scores.items():
    if v > answer:
        answer = v

print(answer)
