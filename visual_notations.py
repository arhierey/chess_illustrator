initial_black0 = ' r #n# b #q# k #b# n #r#'
initial_black1 = '#p# p '*4
initial_white0 = '#R# N #B# Q #K# B #N# R '
initial_white1 = ' P #P#'*4

list_of_nots = ['1.d4', 'Nf6', '2.c4', 'g6', '3.Nc3', 'Bg7', '4.e4', 'd6']

odd_string = '   ###   ###   ###   ###'
even_string = '###   ###   ###   ###   '

w_f = [0, 2, 6, 8, 12, 14, 18, 20]
b_f = [3, 5, 9, 11, 15, 17, 21, 23]

for i in range(0, 24):
    if i in w_f:
        print(odd_string)
    elif i in b_f:
        print(even_string)
    if i == 1:
        print(initial_black0)
    if i == 4:
        print(initial_black1)
    if i == 22:
        print(initial_white0)
    if i == 19:
        print(initial_white1)
