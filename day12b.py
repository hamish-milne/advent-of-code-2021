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
paths: Set[str] = set()
def step(path: List[str], grace: List[str]):
    if path[-1] == 'end':
        paths.add(','.join(path))
        return
    for dst in caves[path[-1]]:
        if dst != 'start' and (dst.isupper() or path.count(dst)-grace.count(dst) < 1):
            step(path + [dst], grace)
for c in caves.keys():
    if not c.isupper() and c not in ('start', 'end'):
        step(['start'], [c])
print(len(paths))