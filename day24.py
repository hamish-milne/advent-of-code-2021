from typing import Any, List, Tuple
import operator

code: List[Tuple[Any, ...]] = [tuple(int(x) if (x.isdigit() or x[1:].isdigit()) else x for x in line.strip().split(' ')) for line in open('day24.txt').readlines()]
vnames = ['w', 'x', 'y', 'z']

def eql(a: int, b: int):
    return 1 if a == b else 0

ops = {
    'add': operator.iadd,
    'mul': operator.imul,
    'div': operator.ifloordiv,
    'mod': operator.imod,
    'eql': eql,
}

def check(ivalues: List[int])->bool:

    state: List[Any] = [0, 0, 0, 0]
    icount = 0

    for tokens in code:
        op = tokens[0]
        s1 = vnames.index(tokens[1])
        v1 = state[s1]
        if op == 'inp':
            if icount < len(ivalues):
                state[s1] = ivalues[icount]
            else:
                state[s1] = (1, 9)
            icount += 1
        else:
            t2 = tokens[2]
            v2 = t2 if type(t2) == int else state[vnames.index(t2)]
            if op == 'add' and v2 == 0:
                continue
            if op == 'add' and v1 == 0:
                state[s1] = v2
                continue
            if op == 'mul' and v2 == 1:
                continue
            if op == 'div' and v2 == 1:
                continue

            opf = ops[op]
            if type(v1) == int and type(v2) == int:
                state[s1] = opf(v1, v2)
                continue
            min1 = v1 if type(v1) == int else v1[0]
            min2 = v2 if type(v2) == int else v2[0]
            max1 = v1 if type(v1) == int else v1[1]
            max2 = v2 if type(v2) == int else v2[1]
            if op == 'mod':
                state[s1] = ((min2+1) if min2 < 0 else 0, (max2-1) if max2 > 0 else 0)
                continue
            if op == 'eql':
                if min2 > max1 or min1 > max2:
                    state[s1] = 0
                elif v1 == v2:
                    state[s1] = 1
                else:
                    state[s1] = (0, 1)
                continue
            perms = [opf(a, b) for (a, b) in [(min1, min2), (min1, max2), (max1, min2), (max1, max2)]]
            minn = min(perms)
            maxn = max(perms)
            if minn == maxn:
                state[s1] = minn
            else:
                state[s1] = (minn, maxn)
    valid = state[3]
    if type(valid) == int:
        return valid == 0
    return 0 in range(valid[0], valid[1]+1)

def calc(start: int, stop: int, step: int):
    ivalues: List[int] = []
    while len(ivalues) < 14:
        ivalues.append(start)
        while not check(ivalues):
            while ivalues[-1] == stop:
                ivalues.pop()
            ivalues[-1] += step
    print(''.join(str(x) for x in ivalues))

calc(9, 1, -1)
calc(1, 9, 1)
