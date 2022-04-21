import random as rnd
from chess_tools import *


def check_coor(coor):
    res = 0
    if coor[0] > 8 or coor[1] > 8:
        res = 1
    elif coor[0] < 1 or coor[1] < 1:
        res = 1
    return res


def field_to_coord(field):
    coord = [0, 0]
    coord[0] = ord(field[0]) - 96
    coord[1] = int(field[1])
    return coord


def on_diagonal(field0, field1):
    coord0 = field_to_coord(field0)
    coord1 = field_to_coord(field1)
    coords = [coord0.copy(), coord0.copy(), coord0.copy(), coord0.copy()]
    res = False
    coord_errors = [0, 0, 0, 0]
    while not all(coord_errors):
        coords[0][0] += 1
        coords[0][1] += 1
        coords[1][0] += -1
        coords[1][1] += -1
        coords[2][0] += 1
        coords[2][1] += -1
        coords[3][0] += -1
        coords[3][1] += 1
        if coords[0] == coord1 or coords[1] == coord1 or coords[2] == coord1 or coords[3] == coord1:
            res = True
        coord_errors = [check_coor(coords[index]) for index in range(0, 4)]
    return res


coord_dict = init_coor_dict(1, 1)
for i in range(0, 100):
    c = [1 + rnd.randint(0, 7), 1 + rnd.randint(0, 7)]
    f0 = coor_to_field(c, coord_dict)
    c = [1 + rnd.randint(0, 7), 1 + rnd.randint(0, 7)]
    f1 = coor_to_field(c, coord_dict)
    print(f0, field_to_coord(f0))
    print(f1, field_to_coord(f1))
    print(on_diagonal(f0, f1))
