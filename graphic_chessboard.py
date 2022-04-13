from graphics import *


def draw_figure(filename, window, coor):
    image = Image(Point(coor[0], coor[1]), filename)
    image.draw(window)
    return 0


win = GraphWin('Board', 500, 500)
win.setBackground('white')

output = draw_figure('tiles/board.png', win, [250, 250])

for i in range(0, 8):
    output = draw_figure('tiles/white_pawn.png', win, [31.25 + i*62.5, 93.75])

win.getMouse()
win.close()
