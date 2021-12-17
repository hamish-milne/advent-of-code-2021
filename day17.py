import re
match = re.match(r'target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)\s*', open('day17.txt').read())
if match is None:
    exit()
[xmin, xmax, ymin, ymax] = [int(x) for x in match.groups()]
maxyvel = -1-ymin
maxypos = (maxyvel*(maxyvel+1))//2
print(maxypos)
