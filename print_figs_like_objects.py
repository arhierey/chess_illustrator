from figures_set import Figures


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


figures = initialize()

