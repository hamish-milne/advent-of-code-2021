input = [int(x) for x in open('day7.txt').read().split(',')]
input.sort()
center = input[len(input) // 2]
print(sum(abs(y - center) for y in input))