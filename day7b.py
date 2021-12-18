input = [int(x) for x in open('day7.txt').read().split(',')]
center = sum(input) // len(input)
def tri(x: int):
    return (x*x + x)//2
print(sum(tri(abs(y - center)) for y in input))