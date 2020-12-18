from math import sqrt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from math import pi
from sympy import *
import z3

class Bot(object):
    def __init__(self, ID, pos, r):
        self.ID = ID
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.x_min, self.x_max = self.x - r, self.x + r
        self.y_min, self.y_max = self.y - r, self.y + r
        self.z_min, self.z_max = self.z - r, self.z + r
        self.xy = (self.x, self.y)
        self.xz = (self.x, self.z)
        self.yz = (self.y, self.z)
        self.r = r

    def __repr__(self):
        string = 'Bot ' + str(self.ID) + ' at position ' + str(self.pos) + ' with radius ' + str(self.r)
        return string


def gen_coord(a, b):
    # check x overlaps
    if not (a.x_min > b.x_max or b.x_min > a.x_max):
        # check if y overlaps
        if not (a.y_min > b.y_max or b.y_min > a.y_max):
            # check if z overlaps
            if not (a.z_min > b.z_max or b.z_min > a.z_max):
                # overlaps in all directions --> check coordinates
                dx = [a.x_min, a.x_max, b.x_min, b.x_max]
                dx.sort()
                dx = tuple(dx[1:-1])  # always take middle 2 points --> draw 4 overlapping circles to see
                dy = [a.y_max, a.y_min, b.y_max, b.y_min]
                dy.sort()
                dy = tuple(dy[1:-1])
                dz = [a.z_max, a.z_min, b.z_max, b.z_min]
                dz.sort()
                dz = tuple(dz[1:-1])
                # print(f'x in {dx}; y in {dy}; z in {dz}')
                coords[(dx, dy, dz)] = (2, [a.ID, b.ID])



with open('input.txt') as f:
    lines = f.read().splitlines()

bots = []

index = 0
for line in lines:
    index_1, index_2 = line.find('<') + 1, line.find('>')
    pos = tuple(map(int, line[index_1:index_2].split(',')))
    r = int(line.split('=')[-1])
    bots.append(Bot(index, pos, r))
    index += 1

# for bot in bots:
#     print(bot)

coords = {}

for a in range(len(bots) - 1):
    for b in range(a + 1, len(bots)):
        gen_coord(bots[a], bots[b])

print(len(coords))
# for k, v in coords.items():
#     print(k, v)


counter = 0

# Equation of sphere = (x - a)² + (y - b)² + (z - c)² = r²






