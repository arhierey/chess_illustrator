import re


filename = 'chess_journal_output.txt'

with open(filename, 'r') as f:
    data = f.read()

words = data.split()

charset = 'abcdefghKQRBN12345678'

matches = []
for w in words:
    if w[0] in charset:
        matches.append(w)

nots = []
patterns = [r'\d[.][abcdefghxKQRBN12345678]', r'[abcdefghxKQRBN]+[12345678]+$', r'\d+[.]']

for i in range(0, len(matches)):
    for pat in patterns:
        if re.match(pat, matches[i]) is not None:
            nots.append(matches[i])

print(nots)
