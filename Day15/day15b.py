import operator
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.finder.dijkstra import DijkstraFinder

class Player:
    def __init__(self, ID, race, pos_x, pos_y, enemies, ap=3):
        self.ID = ID
        self.race = race
        if self.race == 'E':
            self.enemy = 'G'
        else:
            self.enemy = 'E'
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hit_points = 200
        self.attack_power = ap
        self.enemies = enemies

    def move(self):
        # Implement check if already adjacent --> skip
        for delta in (-1, 1):
            if play_board[self.pos_y + delta][self.pos_x] == self.enemy or play_board[self.pos_y][self.pos_x + delta] == self.enemy:
                # Enemy nearby, no need to move
                return None
        # Othrwise start to move
        targets = []
        for enemy in order:
            if enemy.race == self.enemy and enemy.hit_points > 0:
                tar_x = enemy.pos_x
                tar_y = enemy.pos_y
                if play_board[tar_y - 1][tar_x] == '.':
                    targets.append((tar_x, tar_y - 1))
                if play_board[tar_y][tar_x - 1] == '.':
                    targets.append((tar_x - 1, tar_y))
                if play_board[tar_y][tar_x + 1] == '.':
                    targets.append((tar_x + 1, tar_y))
                if play_board[tar_y + 1][tar_x] == '.':
                    targets.append((tar_x, tar_y + 1))
        if len(targets) == 0:
            # No targets, do not move
            return None
        maze = gen_maze((self.pos_x, self.pos_y))
        # Check A* finder
        grid = Grid(matrix=maze)
        start = grid.node(self.pos_x, self.pos_y)
        data = []
        min_path = 99999
        for target in targets:
            end = grid.node(target[0], target[1])
            finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
            path, runs = finder.find_path(start, end, grid)
            Grid.cleanup(grid)
            if len(path) > 1:
                data.append((len(path), path[1][0], path[1][1]))
                if len(path) < min_path:
                    min_path = len(path)
        if len(data) > 0:
            # data.sort(key=operator.itemgetter(0, 2, 1))
            for item in data:
                if item[0] == min_path:
                    play_board[self.pos_y][self.pos_x] = '.'
                    self.pos_x, self.pos_y = item[1], item[2]
                    play_board[self.pos_y][self.pos_x] = self.race
                    break
            # print(f'\n---next step---\n')
            # print(f'{data}\n')
            # print_board(play_board)
            # breakpoint()
        return None

    def attack(self):
        targets = []
        if play_board[self.pos_y - 1][self.pos_x] == self.enemy:
            targets.append((self.pos_x, self.pos_y - 1))
        if play_board[self.pos_y][self.pos_x - 1] == self.enemy:
            targets.append((self.pos_x - 1, self.pos_y))
        if play_board[self.pos_y][self.pos_x + 1] == self.enemy:
            targets.append((self.pos_x + 1, self.pos_y))
        if play_board[self.pos_y + 1][self.pos_x] == self.enemy:
            targets.append((self.pos_x, self.pos_y + 1))
        if len(targets) == 0:
            # No enemies in range
            return None
        else:
            hp = 99999
            cur_enemy = None
            for coord in targets:
                for val in self.enemies:
                    enemy = players[val]
                    enemy_coord = (enemy.pos_x, enemy.pos_y)
                    if coord == enemy_coord and enemy.hit_points < hp:
                        cur_enemy = enemy
                        hp = cur_enemy.hit_points
            # attack
            cur_enemy.hit_points -= self.attack_power
            if cur_enemy.hit_points <= 0:
                # enemy dies
                play_board[cur_enemy.pos_y][cur_enemy.pos_x] = '.'
                del players[cur_enemy.ID]
                if cur_enemy.race == 'E':
                    elfs.remove(cur_enemy.ID)
                else:
                    gobs.remove(cur_enemy.ID)
                # order.remove(cur_enemy)
        return None

def gen_maze(pos):
    maze = []
    for line in play_board:
        maze.append([])
        for char in line:
            if char == '.':
                maze[-1].append(100)
            else:
                maze[-1].append(0)
    factor = 1
    if maze[pos[1] - 1][pos[0]] != 0:
        maze[pos[1] - 1][pos[0]] += factor
        factor += 1
    if maze[pos[1]][pos[0] - 1] != 0:
        maze[pos[1]][pos[0] - 1] += factor
        factor += 1
    if maze[pos[1]][pos[0] + 1] != 0:
        maze[pos[1]][pos[0] + 1] += factor
        factor += 1
    if maze[pos[1] + 1][pos[0]] != 0:
        maze[pos[1] + 1][pos[0]] += factor
    return maze




def print_board(board):
    print('')
    for line in board:
        for char in line:
            print(char, end=',')
        print('')


###################
# Start Main Code #
###################

with open('input.txt') as f:
    lines = f.read().splitlines()

players = {}
elfs = []
gobs = []
number = 0

ap = 40  # Determined iterative

# Set players
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == 'E':
            players[number] = Player(number, lines[y][x], x, y, gobs, ap)
            elfs.append(number)
            number += 1
        elif lines[y][x] == 'G':
            players[number] = Player(number, lines[y][x], x, y, elfs)
            gobs.append(number)
            number += 1
no_of_elfs = len(elfs)
# Set initial board
play_board = []
for line in range(len(lines)):
    play_board.append([])
    for char in lines[line]:
        play_board[line].append(char)
print_board(play_board)

# for k in players.keys():
#     print(f'Player {players[k].ID} is a {players[k].race} at position {players[k].pos_x}, {players[k].pos_y} and enemies {players[k].enemies}')

order = []
finish = False
round = 0
# Start looping from here in a while
# First determine order
while True:
    round += 1
    order.clear()
    order = sorted(players.values(), key=operator.attrgetter('pos_y', 'pos_x'))
    last_player = False
    for player in order:
        if player.ID not in elfs and player.ID not in gobs:
            # Player died this round; pass
            continue
        if player == order[-1]:
            last_player = True
        player.move()
        player.attack()
        # print('\n--- Next move ---\n')
        # print_board(play_board)
        if len(gobs) == 0 or len(elfs) == 0:
            # finished
            finish = True
            break
    # breakpoint()
    print(f'\n--- At round {round} ---')
    print_board(play_board)
    if finish:
        score = 0
        for left_over in players:
            cur_player = players[left_over]
            score += cur_player.hit_points
        if not last_player:
            round -= 1
        print(f'Final score = {score} * {round} = {score * round}')
        print(f'Of {no_of_elfs} Elfs, {no_of_elfs - len(elfs)} elfs died, used ap = {ap}')
        exit()
