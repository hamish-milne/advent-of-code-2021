from typing import Callable
map = [ [int(c) for c in line.strip()] for line in open('day9.txt').readlines() ]
coords = ((y,x,map[y][x]) for y in range(len(map)) for x in range(len(map[0])))
isLowPoint: Callable[[int, int, int], bool] = lambda y,x,p: all((
    True if y == 0 else map[y-1][x] > p,
    True if y+1 >= len(map) else map[y+1][x] > p,
    True if x == 0 else map[y][x-1] > p,
    True if x+1 >= len(map[0]) else map[y][x+1] > p
))
print(sum(
    p+1 if isLowPoint(x,y,p) else 0 for (x,y,p) in coords
))
