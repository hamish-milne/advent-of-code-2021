count = 0
prev = None
for x in open('day1.txt').readlines():
    val = int(x)
    if prev is not None and val > prev:
        count += 1
    prev = val
print(count)
