# Advent of Code 2018 - Day 1
# Part 1 & 2
with open('input.txt') as f:
    lines = f.read().splitlines()

# part 1: Sum up all input; first make all entries ints with the map function
part_1 = sum(list(map(int, lines)))

# part 2: loop over input, stop when a value is reached for 2nd time (multiple loops over input possible)
freq = 0
visited_freq = {freq}  # Use set. Don't use list[<int>, <int>, ...] --> Performance is MUCH slower!
found_2nd = False
i = 0
while True:
    i += 1
    for line in lines:
        freq += int(line)
        if freq not in visited_freq:
            visited_freq.add(freq)
        else:  # 2nd time frequency is found --> Halt
            found_2nd = True
            break
    if found_2nd:
        break

print(f'\n---Part 1---\n')
print(f'The answer to part 1 is {part_1}')
print(f'\n---Part 2---\n')
print(f'The answer to part 2 is {freq} found in the {i}th iteration of the list')
