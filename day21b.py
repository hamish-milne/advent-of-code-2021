from itertools import product, groupby
from typing import Dict, Tuple

die = range(1,4)
scores = [ sum(x) for x in product(die, die, die) ]
scores.sort()
splits = [ (val, len(list(group))) for val,group in groupby(scores) ]

maxscore = 21
places = 10

[p1, p2] = [int(line.split(' ')[-1]) for line in open('day21.txt').readlines()]

univ = { (p1, p2, int(0), int(0)): 1 }
winners = [0, 0]

p = True
while len(univ) > 0:
    univ2: Dict[Tuple[int, int, int, int], int] = {}
    for (p1, p2, s1, s2),n in univ.items():
        pos = p1 if p else p2
        score = s1 if p else s2
        for roll,count in splits:
            newpos = (pos + roll - 1) % places + 1
            newscore = score + newpos
            if newscore >= maxscore:
                winners[0 if p else 1] += count*n
            else:
                state = (newpos, p2, newscore, s2) if p else (p1, newpos, s1, newscore)
                if state not in univ2:
                    univ2[state] = count*n
                else:
                    univ2[state] += count*n
    univ = univ2
    p = not p
print(max(winners))
