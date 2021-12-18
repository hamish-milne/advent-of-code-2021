from typing import Dict, List, Set

caves: Dict[str, Set[str]] = {}
for line in open('day12.txt').readlines():
    [a, b] = line.strip().split('-')
    if a not in caves:
        caves[a] = set()
    if b not in caves:
        caves[b] = set()
    caves[a].add(b)
    caves[b].add(a)
paths: List[List[str]] = []
def step(path: List[str]):
    if path[-1] == 'end':
        paths.append(path)
        return
    for dst in caves[path[-1]]:
        if dst.isupper() or dst not in path:
            step(path + [dst])
step(['start'])
print(len(paths))