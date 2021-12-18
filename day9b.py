from typing import Callable, List, Set, Tuple

map = [ [int(c) for c in line.strip()] for line in open('day9.txt').readlines() ]
coords = ((y,x,map[y][x]) for y in range(len(map)) for x in range(len(map[0])))
isLowPoint: Callable[[int, int, int], bool] = lambda y,x,p: all((
    True if y == 0 else map[y-1][x] > p,
    True if y+1 >= len(map) else map[y+1][x] > p,
    True if x == 0 else map[y][x-1] > p,
    True if x+1 >= len(map[0]) else map[y][x+1] > p
))
basins: List[Set[Tuple[int, int]]] = []
for (y,x,p) in coords:
    if isLowPoint(y,x,p):
        basin: Set[Tuple[int, int]] = set()
        current: Set[Tuple[int, int]] = set()
        current.add((y, x))
        next: Set[Tuple[int, int]] = set()
        while len(current) > 0:
            for (y, x) in current:
                for (y1, x1) in ( (y-1,x), (y+1,x), (y,x-1), (y,x+1) ):
                    if y1 >= 0 and x1 >= 0 and y1 < len(map) and x1 < len(map[0]) and map[y1][x1] < 9 and (y1, x1) not in basin:
                        next.add((y1, x1))
            for t in current:
                basin.add(t)
            current = next
            next = set()
        basins.append(basin)
basinSizes = [len(x) for x in basins]
basinSizes.sort(reverse=True)
print(basinSizes[0] * basinSizes[1] * basinSizes[2])
