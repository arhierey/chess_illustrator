metric = 31.25
step = 2*metric
pairs = []
for i in range(1, 9):
    for j in range(1, 9):
        pairs.append((chr(96 + i) + str(9-j), [metric + (i-1)*step, metric + (j-1)*step]))
coor_dict = dict(pairs)
print(pairs)
print(coor_dict)
