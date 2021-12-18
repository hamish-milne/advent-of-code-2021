fish = [0 for _ in range(9)]
input = [int(x) for x in open('day6.txt').read().split(',')]
for x in input:
    fish[x] += 1
for d in range(256):
    breed = fish.pop(0)
    fish[6] += breed
    fish.append(breed)
print(sum(fish))
