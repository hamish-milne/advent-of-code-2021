from typing import List, Optional, Union, cast
from math import floor, ceil

Pair = List[Union[int, 'Pair']]
LR = (0,1)
RL = (1,0)

def trySplit(n: Pair)->bool:
    for i in LR:
        if type(n[i]) == list:
            if trySplit(cast(Pair, n[i])):
                return True
        else:
            d: int = n[i] # type: ignore
            if d >= 10:
                n[i] = [floor(d/2), ceil(d/2)] # type: ignore
                return True
    return False
def addDigit(n: Pair, i: int, digit: int):
    if type(n[i]) == int:
        n[i] += digit # type: ignore
    else:
        addDigit(cast(Pair, n[i]), i, digit)

def applyExplode(n: Pair, p: List[Optional[int]], i: int)->List[Optional[int]]:
    j = 1 if i == 0 else 0
    if p[j] is not None:
        if type(n[j]) == int:
            n[j] += p[j] # type: ignore
        else:
            addDigit(n[j], i, p[j]) # type: ignore
        p[j] = None  # type: ignore
    return p

def tryExplode(n: Pair, nest: int)->Optional[List[Optional[int]]]:
    for i in LR:
        if type(n[i]) == list:
            p = cast(Pair, n[i])
            if nest == 3:
                if all(type(p[x]) == int for x in (0,1)):
                    n[i] = 0
                    return applyExplode(n, p, i) # type: ignore
            else:
                ret = tryExplode(p, nest+1)
                if ret is not None:
                    return applyExplode(n, ret, i)

def magnitude(n: Union[int, Pair])->int:
    if type(n) == int:
        return n # type: ignore
    return magnitude(n[0])*3 + magnitude(n[1])*2 # type: ignore

def add(a: Pair, b: Pair):
    ret: Pair = [a, b]
    while (tryExplode(ret, 0) is not None) or trySplit(ret):
        pass
    return ret

if __name__ == '__main__':
    acc: Pair = None # type: ignore
    for line in open('day18.txt').readlines():
        n: Pair = eval(line)
        if acc is None:
            acc = n
        else:
            acc = add(acc, n)
    print(magnitude(acc))