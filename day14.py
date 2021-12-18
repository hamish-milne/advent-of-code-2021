f = open('day14.txt')
template = list(f.readline().strip())
f.readline()
rules = {tuple(r[0]):r[1] for r in [line.strip().split(' -> ') for line in f.readlines()]}
for s in range(10):
    i = 0
    while i < len(template)-1:
        pair = (template[i], template[i+1])
        if pair in rules:
            template.insert(i+1, rules[pair])
            i += 1
        i += 1
counts = [template.count(k) for k in set(template)]
print(max(counts) - min(counts))
