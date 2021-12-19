
from typing import List, Literal, Set, Tuple, Type, cast
from numpy import array, ndarray, dtype, int32, cross, subtract, matmul, round
from itertools import permutations, combinations
from numpy.core.fromnumeric import transpose
from numpy.lib.arraypad import pad
from numpy.linalg import inv

Vector3 = Type['ndarray[Tuple[Literal[3]], dtype[int32]]']
Vector4 = Type['ndarray[Tuple[Literal[4]], dtype[int32]]']
Matrix = Type['ndarray[Tuple[Literal[4], Literal[4]], dtype[int32]]']
scanners = [
    [
        cast(Vector3, array([ int(x) for x in line.split(',') ]))
        for line in group.splitlines()[1:]
    ]
    for group in open('day19.txt').read().split('\n\n')
] 

def axis(n: int, v: int):
    l = [0, 0, 0]
    l[n] = v
    return cast(Vector4, array(l))
orientations = [
    cast(Matrix, array([
        axis(face, fdir),
        axis(up, updir),
        cast(Vector3, cross(axis(face, fdir), axis(up, updir))),
    ]))
    for updir in (1, -1)
    for fdir in (1, -1)
    for (face, up) in permutations(range(3), 2)
]

def calcOffsets():
    for (s0i, s1i) in combinations(range(len(scanners)), 2):
        s0 = scanners[s0i]
        s1 = scanners[s1i]
        found = False
        for o in orientations:
            s1r: List[Vector3] = [o.dot(b1) for b1 in s1] # type: ignore
            for b1 in s1r:
                deltas1 = [subtract(b, b1) for b in s1r]
                for b0 in s0:
                    deltas0 = [subtract(b, b0) for b in s0]
                    l = len(set(tuple(x) for x in deltas0).intersection(tuple(x) for x in deltas1))
                    if l >= 12:
                        d = subtract(b0, b1)
                        d.resize((4,))
                        d[3] = 1
                        m: Matrix = pad(transpose(o), [(0, 1), (0, 1)], mode='constant')
                        m[3] = d # type: ignore
                        print(str(s1i)+' relative to '+str(s0i))
                        print(m)
                        print('')
                        yield (s1i, s0i, cast(Matrix, m))
                        invm = round(inv(m)).astype(int32) # type: ignore
                        print(invm) # type: ignore
                        yield (s0i, s1i, cast(Matrix, invm))
                        found = True
                        break
                if found:
                    break
            if found:
                break
offsets = list(calcOffsets())

offsetMap = {t[0]:t[2] for t in offsets if t[1] == 0}
while len(offsetMap) < len(scanners)-1:
    for (s1i, s0i, ma) in offsets:
        if s1i in offsetMap or s0i not in offsetMap:
            continue
        mb = offsetMap[s0i]
        mx = matmul(ma, mb)
        
        print('Using '+str(s0i)+', '+str(s1i)+' relative to 0')
        print(mx)
        print('')
        offsetMap[s1i] = mx
bset: Set[Vector3] = set()
for si in range(len(scanners)):
    s = scanners[si]
    for b in s:
        m = offsetMap[si]
        bp = b.copy() # type: ignore
        bp.resize((4,)) # type: ignore
        bp[3] = 1
        bset.add(tuple(bp.dot(m))) # type: ignore
blist = list(bset)
blist.sort()
print(str(blist).replace('), (', '\n'))
print(len(bset))

print(max(
    sum(abs(offsetMap[a][3] - offsetMap[b][3])) # type: ignore
for (a, b) in combinations(range(len(scanners)), 2) ))
