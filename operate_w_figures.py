from figures_set import Figures
import re


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

    return figs


def get_move(notation):
    res = re.search(r'[abcdefgh][12345678]$', notation)
    return res.group()


def get_fig(notation):
    res = re.search(r'[KQRBN]', notation)
    if res is None:
        return 'p'
    return res.group()


def moving_pawn(move, figures_dict, wb):
    if wb == 0:
        letter = 'P'
    else:
        letter = 'p'
    res = letter
    for key in figures_dict.keys():
        if key[0] == letter and figures_dict[key].coor[0] == move[0]:
            res += key[1]
            break
    return res


list_of_nots = ['1.d4', 'Nf6', '2.c4', 'g6', '3.Nc3', 'Bg7', '4.e4', 'd6']

figures = initialize()

print(figures)

m, f = '', ''
not_pawns = ['r', 'R', 'b', 'B', 'n', 'N']
for i in range(0, len(list_of_nots)):
    m = get_move(list_of_nots[i])
    f = get_fig(list_of_nots[i])
    if i % 2 == 0:
        if f == 'p':
            figures[moving_pawn(m, figures, 0)].move(m)
    else:
        if f == 'p':
            figures[moving_pawn(m, figures, 1)].move(m)

print('end')
