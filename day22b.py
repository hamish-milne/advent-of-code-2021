import re
from typing import List

cubes: List[List[int]] = []

for line in open('day22.txt').readlines():
    c = [
        (int(x) if x not in ('on','off') else (1 if x == 'on' else -1))
        for x in
        re.match(r'(o\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)\s*', line).groups() # type: ignore
    ]
    for i in range(len(cubes)):
        ci = cubes[i]
        x = [
            -ci[0],
            max(c[1], ci[1]),
            min(c[2], ci[2]),
            max(c[3], ci[3]),
            min(c[4], ci[4]),
            max(c[5], ci[5]),
            min(c[6], ci[6])
        ]
        if x[1] > x[2] or x[3] > x[4] or x[5] > x[6]:
            continue
        cubes.append(x)
    if c[0] > 0:
        cubes.append(c)
print(sum(c[0]*(1+c[2]-c[1])*(1+c[4]-c[3])*(1+c[6]-c[5]) for c in cubes))
