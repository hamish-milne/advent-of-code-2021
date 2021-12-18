input = open('day3.txt').readlines()
width = len(input[0].strip())
length = len(input)
gamma = 0
for i in range(width):
    d = 1 if sum((int(l[i]) for l in input)) >= length/2 else 0
    gamma += d << (width - 1 - i)
epsilon = (~gamma) & (1 << width)-1
print(gamma * epsilon)
