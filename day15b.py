from typing import Dict, Set, Tuple

grid = [[int(c) for c in line.strip()] for line in open('day15.txt').readlines()]
size = len(grid)
rep = 5

Node = Tuple[int, int]

def eval(pos: Node):
    add = pos[0]//size + pos[1]//size
    val = grid[pos[0]%size][pos[1]%size] + add
    while val > 9:
        val -= 9
    return val

parents: Dict[Node, int] = {(0, 0): 0}
l_open: Set[Node] = set([(0, 0)])
l_closed: Set[Node] = set()

target = ((rep*size)-1, (rep*size)-1)

def gcost(pos: Node):
    return parents[pos] + eval(pos)

def hcost(pos: Node):
    return abs(pos[0]-target[0]) + abs(pos[1]-target[1])

def fcost(pos: Node):
    return gcost(pos) + hcost(pos)

adjacents = [(0, 1), (-1, 0), (0, -1), (1, 0)]

while True:
    current = min(l_open, key=fcost)
    ccost = gcost(current)
    if current == target:
        print(gcost(current) - eval((0, 0)))
        break
    l_closed.add(current)
    l_open.remove(current)

    for offset in adjacents:
        adj = (current[0]+offset[0], current[1]+offset[1])
        if adj in l_closed or adj[0] < 0 or adj[1] < 0 or adj[0] > target[0] or adj[1] > target[1]:
            continue
        # Since we just need the score, no need to track the path itself
        if adj in l_open:
            parents[adj] = min(parents[adj], ccost)
        else:
            l_open.add(adj)
            parents[adj] = ccost
