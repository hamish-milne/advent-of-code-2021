f = open('day14.txt')
template = f.readline().strip()
f.readline()
rules = [(r[0], ''.join([r[0][0], r[1]]), ''.join([r[1], r[0][1]])) for r in [line.strip().split(' -> ') for line in f.readlines()]]
counts = {k:0 for k in set(item for sublist in rules for item in sublist)}
for i in range(len(template)-1):
    pair = template[i:i+2]
    counts[pair] += 1
for _ in range(40):
    ncounts = {**counts}
    for (k, a, b) in rules:
        kcount = counts[k]
        ncounts[a] += kcount
        ncounts[b] += kcount
        ncounts[k] -= kcount
    counts = ncounts
def sum_pos(l: str, i: int):
    return sum(v for (k,v) in counts.items() if k[i] == l)
lcounts = {k:max(sum_pos(k, i) for i in range(2)) for k in set(''.join(counts.keys()))}
print(max(lcounts.values()) - min(lcounts.values()))
