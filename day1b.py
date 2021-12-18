values = [int(x) for x in open('day1.txt').readlines()]
count = 0
prev = None
WINDOW = 3
for i in range(len(values) - (WINDOW - 1)):
    val = sum([values[i + j] for j in range(WINDOW)])
    if prev is not None and val > prev:
        count += 1
    prev = val
print(count)
