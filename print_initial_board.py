from graphics import *


def draw_figure(filename, window, coor):
    image = Image(Point(coor[0], coor[1]), filename)
    image.draw(window)


def init_coor_dict(metric, step):
    metric = 31.25
    step = 2 * metric
    pairs = []
    for i in range(1, 9):
        for j in range(1, 9):
            pairs.append((chr(96 + i) + str(9 - j), [metric + (i - 1) * step, metric + (j - 1) * step]))
    coor_dict = dict(pairs)
    return coor_dict


coor_dict = init_coor_dict(31.25, 62.5)

win = GraphWin('Board', 500, 500)

draw_figure('tiles/board.png', win, [250, 250])

for i in range(0, 8):
    draw_figure('tiles/white_pawn.png', win, [31.25 + i*62.5, 406.25])
    draw_figure('tiles/black_pawn.png', win, [31.25 + i*62.5, 93.75])

draw_figure('tiles/white_rook.png', win, coor_dict['a1'])
draw_figure('tiles/white_rook.png', win, coor_dict['h1'])
draw_figure('tiles/black_rook.png', win, coor_dict['a8'])
draw_figure('tiles/black_rook.png', win, coor_dict['h8'])
draw_figure('tiles/white_knight.png', win, coor_dict['b1'])
draw_figure('tiles/white_knight.png', win, coor_dict['g1'])
draw_figure('tiles/black_knight.png', win, coor_dict['b8'])
draw_figure('tiles/black_knight.png', win, coor_dict['g8'])
draw_figure('tiles/white_bishop.png', win, coor_dict['c1'])
draw_figure('tiles/white_bishop.png', win, coor_dict['f1'])
draw_figure('tiles/black_bishop.png', win, coor_dict['c8'])
draw_figure('tiles/black_bishop.png', win, coor_dict['f8'])
draw_figure('tiles/white_king.png', win, coor_dict['e1'])
draw_figure('tiles/black_king.png', win, coor_dict['e8'])
draw_figure('tiles/white_queen.png', win, coor_dict['d1'])
draw_figure('tiles/black_queen.png', win, coor_dict['d8'])

win.getMouse()
win.close()
