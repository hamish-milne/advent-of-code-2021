from itertools import product
import re
from typing import Set, Tuple
input = [
    [
        (int(x) if x not in ('on','off') else (x == 'on'))
        for x in
        re.match(r'(o\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)\s*', line).groups() # type: ignore
    ] for line in open('day22.txt').readlines()
]

state: Set[Tuple[int, int, int]] = set()
for c in input:
    if any(abs(x) > 50 for x in c):
        break
    cubes = product(range(c[1],c[2]+1), range(c[3],c[4]+1), range(c[5],c[6]+1))
    if c[0]:
        for x in cubes:
            state.add(x)
    else:
        for x in cubes:
            if x in state:
                state.remove(x)

print(len(state))
