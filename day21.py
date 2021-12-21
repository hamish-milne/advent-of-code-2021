positions = [int(line.split(' ')[-1]) for line in open('day21.txt').readlines()]
scores = [0, 0]
die = 1
rcount = 0
def roll():
    global die
    global rcount
    rcount += 1
    val = die
    die = (die % 10) + 1
    return val
p = 0
while not any(s >= 1000 for s in scores):
    val = roll()+roll()+roll()
    positions[p] = ((positions[p] + val - 1) % 10) + 1
    scores[p] += positions[p]
    p = (p + 1) % 2
print(scores[p]*rcount)
