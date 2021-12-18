directions = {
    'forward': [1, 0],
    'down': [0, 1],
    'up': [0, -1]
}
x = 0
y = 0
for line in open('day2.txt').readlines():
    [direction, amount] = line.split(' ')
    [xmul, ymul] = directions[direction]
    val = int(amount)
    x += xmul * val
    y += ymul * val
print(x * y)
