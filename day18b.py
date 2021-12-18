from day18 import add, magnitude
from itertools import permutations
print(max(magnitude(add(eval(a), eval(b))) for (a, b) in permutations(open('day18.txt').readlines(), 2)))
