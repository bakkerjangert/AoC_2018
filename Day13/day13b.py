import operator

class Cart:
    def __init__(self, number, direction, pos_x, pos_y, init_char):
        self.number = number
        self.direction = direction
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.init_char = init_char
        self.counter = 0


with open('input.txt') as f:
    lines = f.read().splitlines()

directions = '^<>v'
cart_tot = 0
init_string = '|--|--||--|-||-|-'  # See print statements below; added manually
# init_string = '-|'

for line in lines:
    cart_tot += line.count('^') + line.count('<') + line.count('>') + line.count('v')
    print(line)

carts = {}
number = 1
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] in directions:
            carts[number] = Cart(number, lines[y][x], x, y, init_string[number - 1])
            number += 1

for k, v in carts.items():
    print('cart no', carts[k].number, 'is at position', carts[k].pos_x, 'by', carts[k].pos_y , 'and facing in', carts[k].direction)

# for k in carts.keys():
#     print('Start position of cart', carts[k].number)
#     print(lines[carts[k].pos_y - 1][carts[k].pos_x - 1], lines[carts[k].pos_y - 1][carts[k].pos_x], lines[carts[k].pos_y - 1][carts[k].pos_x + 1])
#     print(lines[carts[k].pos_y][carts[k].pos_x - 1], lines[carts[k].pos_y][carts[k].pos_x], lines[carts[k].pos_y][carts[k].pos_x + 1])
#     print(lines[carts[k].pos_y + 1][carts[k].pos_x - 1], lines[carts[k].pos_y + 1][carts[k].pos_x], lines[carts[k].pos_y + 1][carts[k].pos_x + 1])
#     print('-' * 10)

order = []

while True:
    # Loop from here in a while.

    # First determine order
    order.clear()
    for car in (sorted(carts.values(), key=operator.attrgetter('pos_y', 'pos_x'))):
        order.append(car.number)

    for car in order:
        if car not in carts.keys():
            continue
        # Read data
        direction = carts[car].direction
        pos_x = carts[car].pos_x
        pos_y = carts[car].pos_y
        counter = carts[car].counter
        init_char = carts[car].init_char
        number = carts[car].number

        # Determine next char
        if direction == '^':
            next_char = lines[pos_y - 1][pos_x]
            next_x = pos_x
            next_y = pos_y - 1
            if next_char == '\\':
                next_dir = '<'
            elif next_char == '/':
                next_dir = '>'
            elif next_char == '+':
                if counter == 0:
                    next_dir = '<'
                    counter += 1
                elif counter == 1:
                    next_dir = '^'
                    counter += 1
                elif counter == 2:
                    next_dir = '>'
                    counter = 0
            else:
                next_dir = '^'
            if next_char in directions:
                # Crash!
                print('crash at position', next_x, next_y)
                lines[pos_y] = lines[pos_y][:pos_x] + init_char + lines[pos_y][pos_x + 1:]
                for k, v in carts.items():
                    if carts[k].pos_x == next_x and carts[k].pos_y == next_y:
                        init_char = carts[k].init_char
                        del_num = carts[k].number
                lines[next_y] = lines[next_y][:next_x] + init_char + lines[next_y][next_x + 1:]
                del carts[del_num]
                del carts[number]
                if len(carts) == 1:
                    for k in carts:
                        print('Position of last cart is', carts[k].pos_x, carts[k].pos_y)
            next_init = lines[pos_y - 1][pos_x]

        elif direction == '<':
            next_char = lines[pos_y][pos_x - 1]
            next_x = pos_x - 1
            next_y = pos_y
            if next_char == '\\':
                next_dir = '^'
            elif next_char == '/':
                next_dir = 'v'
            elif next_char == '+':
                if counter == 0:
                    next_dir = 'v'
                    counter += 1
                elif counter == 1:
                    next_dir = '<'
                    counter += 1
                elif counter == 2:
                    next_dir = '^'
                    counter = 0
            else:
                next_dir = '<'
            if next_char in directions:
                # Crash!
                print('crash at position', next_x, next_y)
                lines[pos_y] = lines[pos_y][:pos_x] + init_char + lines[pos_y][pos_x + 1:]
                for k, v in carts.items():
                    if carts[k].pos_x == next_x and carts[k].pos_y == next_y:
                        init_char = carts[k].init_char
                        del_num = carts[k].number
                lines[next_y] = lines[next_y][:next_x] + init_char + lines[next_y][next_x + 1:]
                del carts[del_num]
                del carts[number]
                if len(carts) == 1:
                    for k in carts:
                        print('Position of last cart is', carts[k].pos_x, carts[k].pos_y)
            next_init = lines[pos_y][pos_x - 1]

        elif direction == '>':
            next_char = lines[pos_y][pos_x + 1]
            next_x = pos_x + 1
            next_y = pos_y
            if next_char == '\\':
                next_dir = 'v'
            elif next_char == '/':
                next_dir = '^'
            elif next_char == '+':
                if counter == 0:
                    next_dir = '^'
                    counter += 1
                elif counter == 1:
                    next_dir = '>'
                    counter += 1
                elif counter == 2:
                    next_dir = 'v'
                    counter = 0
            else:
                next_dir = '>'

            if next_char in directions:
                # Crash!
                print('crash at position', next_x, next_y)
                lines[pos_y] = lines[pos_y][:pos_x] + init_char + lines[pos_y][pos_x + 1:]
                for k, v in carts.items():
                    if carts[k].pos_x == next_x and carts[k].pos_y == next_y:
                        init_char = carts[k].init_char
                        del_num = carts[k].number
                lines[next_y] = lines[next_y][:next_x] + init_char + lines[next_y][next_x + 1:]
                del carts[del_num]
                del carts[number]
                if len(carts) == 1:
                    for k in carts:
                        print('Position of last cart is', carts[k].pos_x, carts[k].pos_y)
            next_init = lines[pos_y][pos_x + 1]

        elif direction == 'v':
            next_char = lines[pos_y + 1][pos_x]
            next_x = pos_x
            next_y = pos_y + 1
            if next_char == '\\':
                next_dir = '>'
            elif next_char == '/':
                next_dir = '<'
            elif next_char == '+':
                if counter == 0:
                    next_dir = '>'
                    counter += 1
                elif counter == 1:
                    next_dir = 'v'
                    counter += 1
                elif counter == 2:
                    next_dir = '<'
                    counter = 0
            else:
                next_dir = 'v'
            if next_char in directions:
                # Crash!
                print('crash at position', next_x, next_y)
                lines[pos_y] = lines[pos_y][:pos_x] + init_char + lines[pos_y][pos_x + 1:]
                for k, v in carts.items():
                    if carts[k].pos_x == next_x and carts[k].pos_y == next_y:
                        init_char = carts[k].init_char
                        del_num = carts[k].number
                lines[next_y] = lines[next_y][:next_x] + init_char + lines[next_y][next_x + 1:]
                del carts[del_num]
                del carts[number]
                if len(carts) == 1:
                    for k in carts:
                        print('Position of last cart is', carts[k].pos_x, carts[k].pos_y)
            next_init = lines[pos_y + 1][pos_x]

        if car not in carts.keys():
            continue

        # Change board
        lines[next_y] = lines[next_y][:next_x] + next_dir + lines[next_y][next_x + 1:]
        lines[pos_y] = lines[pos_y][:pos_x] + init_char + lines[pos_y][pos_x + 1:]

        # Update date
        carts[car].direction = next_dir
        carts[car].pos_x = next_x
        carts[car].pos_y = next_y
        carts[car].counter = counter
        carts[car].init_char = next_init

        # for line in lines:
        #     print(line)
        # print('Press enter to continue')
        # input()

