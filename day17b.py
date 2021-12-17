import re
match = re.match(r'target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)\s*', open('day17.txt').read())
if match is None:
    exit()
[xmin, xmax, ymin, ymax] = [int(x) for x in match.groups()]
def valid(vx: int, vy: int):
    (px, py) = 0, 0
    i = 0
    while px <= xmax and py >= ymin:
        if px >= xmin and py <= ymax:
            return True
        px += vx
        py += vy
        vy -= 1
        if vx > 0:
            vx -= 1
        i += 1
    return False
print(sum(1 if valid(x, y) else 0 for y in range(ymin, -ymin) for x in range(0, xmax+1)))