from itertools import permutations
from typing import Set

input = [
    [tuple(
        ord(c)-ord('a') for c in y.strip()
        ) for y in x.split(' ')
    ] for x in open('day8.txt').readlines()
]
digits = [
    0b1110111,
    0b0100100,
    0b1011101,
    0b1101101,
    0b0101110,
    0b1101011,
    0b1111011,
    0b0100101,
    0b1111111,
    0b1101111,
]
perms = [x for x in permutations(range(7))]
found: Set[int] = set()
total = 0
for line in input:
    for p in perms:
        found.clear()
        for word in (line[i] for i in range(10)):
            digit = 0
            for c in word:
                digit |= 1 << p.index(c)
            if digit not in digits or digit in found:
                break
            found.add(digit)
        if len(found) == 10:
            value = 0
            for word in (line[i] for i in range(11, 15)):
                digit = 0
                for c in word:
                    digit |= 1 << p.index(c)
                value = (value * 10) + digits.index(digit)
            total += value
            break
print(total)
