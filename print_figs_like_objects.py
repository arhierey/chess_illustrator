from figures_set import Figures
from graphics import *


def set_colours(fig_dict):
    for key in fig_dict.keys():
        if key[0].lower() == key[0]:
            fig_dict[key].set_colour('black')
        else:
            fig_dict[key].set_colour('white')


def set_start_coors(fig_dict):
    for key in fig_dict.keys():
        if key[0] == 'p':
            fig_dict[key].set_coor(chr(97+int(key[1])) + '7')
        elif key[0] == 'P':
            fig_dict[key].set_coor(chr(97+int(key[1])) + '2')
        elif key[0] == 'n':
            if key[1] == '0':
                fig_dict[key].set_coor('b8')
            else:
                fig_dict[key].set_coor('g8')
        elif key[0] == 'N':
            if key[1] == '0':
                fig_dict[key].set_coor('b1')
            else:
                fig_dict[key].set_coor('g1')
        elif key[0] == 'r':
            if key[1] == '0':
                fig_dict[key].set_coor('a8')
            else:
                fig_dict[key].set_coor('h8')
        elif key[0] == 'R':
            if key[1] == '0':
                fig_dict[key].set_coor('a1')
            else:
                fig_dict[key].set_coor('h1')
        elif key[0] == 'b':
            if key[1] == '0':
                fig_dict[key].set_coor('c8')
            else:
                fig_dict[key].set_coor('f8')
        elif key[0] == 'B':
            if key[1] == '0':
                fig_dict[key].set_coor('c1')
            else:
                fig_dict[key].set_coor('f1')
        elif key[0] == 'q':
            fig_dict[key].set_coor('d8')
        elif key[0] == 'Q':
            fig_dict[key].set_coor('d1')
        elif key[0] == 'k':
            fig_dict[key].set_coor('e8')
        elif key[0] == 'K':
            fig_dict[key].set_coor('e1')


def set_images(fig_dict, images):
    for key in fig_dict.keys():
        fig_dict[key].set_image(images[key[0]])


def init_images_dict():
    b = 'tiles/black_'
    w = 'tiles/white_'
    e = '.png'
    pairs = []
    pairs.append(['p', b + 'pawn' + e])
    pairs.append(['P', w + 'pawn' + e])
    pairs.append(['q', b + 'queen' + e])
    pairs.append(['Q', w + 'queen' + e])
    pairs.append(['k', b + 'king' + e])
    pairs.append(['K', w + 'king' + e])
    pairs.append(['r', b + 'rook' + e])
    pairs.append(['R', w + 'rook' + e])
    pairs.append(['b', b + 'bishop' + e])
    pairs.append(['B', w + 'bishop' + e])
    pairs.append(['n', b + 'knight' + e])
    pairs.append(['N', w + 'knight' + e])

    images_dict = dict(pairs)
    return images_dict


def initialize():
    names = ['p'+str(i) for i in range(0, 8)]
    names.extend(['P'+str(i) for i in range(0, 8)])
    names.extend(['q', 'Q', 'k', 'K'])
    names.extend(['N'+str(i) for i in range(0, 2)])
    names.extend(['R'+str(i) for i in range(0, 2)])
    names.extend(['r'+str(i) for i in range(0, 2)])
    names.extend(['n'+str(i) for i in range(0, 2)])
    names.extend(['B'+str(i) for i in range(0, 2)])
    names.extend(['b'+str(i) for i in range(0, 2)])

    pairs = [(names[i], Figures(names[i])) for i in range(0, 32)]

    figs = dict(pairs)

    for i in range(0, 8):
        figs['p'+str(i)].set_colour('black')
        figs['p'+str(i)].set_coor(chr(97+i) + '7')
        figs['P' + str(i)].set_colour('white')
        figs['P' + str(i)].set_coor(chr(97+i) + '2')

    set_colours(figs)
    set_start_coors(figs)

    for key in figs.keys():
        figs[key].eaten_status(False)

    return figs


def print_figures(fig_dict, win, coor_dict):
    for key in fig_dict.keys():
        draw_figure(fig_dict[key].image, win, coor_dict[fig_dict[key].coor])


def draw_figure(filename, window, coor):
    image = Image(Point(coor[0], coor[1]), filename)
    image.draw(window)


def init_coor_dict(metric, step):
        pairs = []
        for i in range(1, 9):
            for j in range(1, 9):
                pairs.append((chr(96 + i) + str(9 - j), [metric + (i - 1) * step, metric + (j - 1) * step]))
        coor_dict = dict(pairs)
        return coor_dict


coor_dict = init_coor_dict(31.25, 62.5)

figures = initialize()
images = init_images_dict()
set_images(figures, images)

win = GraphWin('Board', 500, 500)
draw_figure('tiles/board.png', win, [250, 250])

print_figures(figures, win, coor_dict)

win.getMouse()
win.close()
