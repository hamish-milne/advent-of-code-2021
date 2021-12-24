from typing import Dict, Iterator, List, Optional, Set, Tuple, cast

Amphipod = int
Room = Tuple[Amphipod, ...]
Hall = Tuple[Optional[Amphipod], ...]
State = Tuple[Room, Room, Room, Room, Hall]

s: List[int] = []
for c in open('day23.txt').read():
    i = ord(c)-ord('A')
    if i in range(4):
        s.append(i)
StartState: State = ((s[4], s[0]), (s[5], s[1]), (s[6], s[2]), (s[7], s[3]), (None,)*7)
L = 2
EndState: State = ((0,)*L, (1,)*L, (2,)*L, (3,)*L, (None,)*7)

TO_ROOM = 0
TO_HALL = 1
Move = Tuple[int, int, int, int]

Node = Tuple[State, int, Optional['Node']]

def get_moves(state: State)->Iterator[Move]:
    hall = state[4]
    for ri in range(4):
        room = cast(Room, state[ri])
        left = (ri+1, -1, -1)
        right = (ri+2, len(hall), 1)
        for (start, stop, step) in (left, right):
            for hi in range(start, stop, step):
                moves = (L - len(room)) + 2*(1 + (hi - start)*step)
                if hi in (0,len(hall)-1):
                    moves -= 1
                if hall[hi] is not None:
                    if hall[hi] == ri and (len(room) == 0 or (len(room) == 1 and room[-1] == ri)):
                        yield (hi, TO_ROOM, ri, (moves-1) * (10 ** hall[hi])) # type: ignore
                    break
                elif len(room) > 0 and (room[-1] != ri or (len(room) > 1 and room[-2] != ri)):
                    yield (ri, TO_HALL, hi, moves * (10 ** room[-1]))

def make_move(state: State, move: Move)->State:
    hall = list(state[4])
    rooms = list(state)
    if move[1] == TO_ROOM:
        a = cast(Amphipod, hall[move[0]])
        rooms[move[2]] += (a,)
        hall[move[0]] = None
    else: # TO_HALL
        hall[move[2]] = rooms[move[0]][-1]
        rooms[move[0]] = rooms[move[0]][:-1]
    rooms[4] = tuple(hall)
    return cast(State, tuple(rooms))

def print_one(a: Optional[Amphipod]):
    if a is None:
        print('.', end='', flush=False)
    else:
        print(chr(ord('A')+a), end='', flush=False)

def print_state(state: State):
    print('#############', flush=False)
    print('#', end='', flush=False)
    
    hall = state[4]
    print_one(hall[0])
    print_one(hall[1])
    print('.', end='', flush=False)
    print_one(hall[2])
    print('.', end='', flush=False)
    print_one(hall[3])
    print('.', end='', flush=False)
    print_one(hall[4])
    print('.', end='', flush=False)
    print_one(hall[5])
    print_one(hall[6])

    print('#', flush=False)
    for p in range(L-1, -1, -1):
        print('###' if p == L-1 else '  #', end='', flush=False)
        for ri in range(4):
            print_one(None if len(state[ri]) <= p else state[ri][p])
            print('#', end='', flush=False)
        print('##' if p == L-1 else '  ', flush=False)
    print('  #########  \n')

l_closed: Set[State] = set()
l_open: Dict[State, Node] = {}

def gcost(node: Node):
    return node[1]

def hcost(node: Node):
    c = 0
    # for ri in range(4):
    #     for a in cast(Room, node[0][ri]):
    #         if a != ri:
    #             c += a * 2 * (1 + abs(a - ri))
    # for hi in range(7):
    #     a = node[0][4][hi]
    #     if a is None:
    #         continue
    #     rhi = 2 * (1 + a)
    #     c += a * (1 + abs(hi - rhi))
    return c

def fcost(node: Node):
    return gcost(node) + hcost(node)

l_open[StartState] = (StartState, 0, None)

while True:
    current = min(l_open.values(), key=fcost)
    if current[0] == EndState:
        print(gcost(current))
        while current is not None:
            print(current[1])
            print_state(current[0])
            current = current[2]
        break
    l_closed.add(current[0])
    del l_open[current[0]]

    for move in get_moves(current[0]):
        adj = make_move(current[0], move)
        if adj in l_closed:
            continue
        ccost = gcost(current) + move[3]
        if adj in l_open:
            if ccost < l_open[adj][1]:
                l_open[adj] = (adj, ccost, current)
        else:
            l_open[adj] = (adj, ccost, current)
