from typing import Callable, Dict, Tuple
sign: Callable[[int], int] = lambda x: x and (1, -1)[x<0]
input = [ tuple( tuple(int(x) for x in y.split(',')) for y in z.split(' -> ') ) for z in open('day5.txt').readlines() ]
points: Dict[Tuple[int, ...], int] = {}
for (a, b) in input:
    points[a] = (points.get(a) or 0) + 1
    while a != b:
        a = (a[0] + sign(b[0] - a[0]), a[1] + sign(b[1] - a[1]))
        points[a] = (points.get(a) or 0) + 1
print(sum(1 for x in points.values() if x >= 2))
