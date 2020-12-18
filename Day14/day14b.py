# Why list? String is sufficient

board = []

# Set in values

board.append(3)
board.append(7)

pos_elf_1 = 0
pos_elf_2 = 1

new_recipe = board[pos_elf_1] + board[pos_elf_2]

total_rec = 330121

while True:
    if new_recipe >= 10:
        new_rec_1 = int(str(new_recipe)[0])
        new_rec_2 = int(str(new_recipe)[1])
    else:
        new_rec_1 = new_recipe
        new_rec_2 = '-'

    board.append(new_rec_1)

    if new_rec_2 != '-':
        board.append(new_rec_2)

    # Ommit if by first calculating new position and then apply % len(board)
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

    if len(board) > 10:
        temp = ''.join(str(x) for x in board[-7:])
        num = temp.find(str(total_rec))
        if num >= 0:
            print('The answer is', len(board) - len(temp) + num)
            quit()
    if len(board) % 100000 == 0:
        print('Current recipe is', len(board))

    if len(board) >= 20216138 + 1000:
        print('Recipe not found, check your code!')
        quit()
