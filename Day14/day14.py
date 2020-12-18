board = []

# Set in values

board.append(3)
board.append(7)

pos_elf_1 = 0
pos_elf_2 = 1

new_recipe = board[pos_elf_1] + board[pos_elf_2]

total_rec = 330121

while len(board) < total_rec + 15:
    if new_recipe >= 10:
        new_rec_1 = int(str(new_recipe)[0])
        new_rec_2 = int(str(new_recipe)[1])
    else:
        new_rec_1 = new_recipe
        new_rec_2 = '-'

    board.append(new_rec_1)

    if new_rec_2 != '-':
        board.append(new_rec_2)

    step_elf_1 = (board[pos_elf_1] + 1) % len(board)
    step_elf_2 = (board[pos_elf_2] + 1) % len(board)

    if step_elf_1 + pos_elf_1 >= len(board):
        pos_elf_1 = step_elf_1 + pos_elf_1 - len(board)
    else:
        pos_elf_1 = pos_elf_1 + step_elf_1

    if step_elf_2 + pos_elf_2 >= len(board):
        pos_elf_2 = pos_elf_2 + step_elf_2 - len(board)
    else:
        pos_elf_2 = pos_elf_2 + step_elf_2
    new_recipe = board[pos_elf_1] + board[pos_elf_2]

    if len(board) % 1000 == 0:
        print('Processing recipe', len(board))

answer = []
for i in range(total_rec, total_rec + 10):
    answer.append(board[i])

print('The answer is', answer)
