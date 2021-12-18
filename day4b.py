from typing import Set
input = open('day4.txt').read().split('\n\n')
draw = [int(x) for x in input[0].split(',')]
input.pop(0)
boards = [[int(y) for y in x.replace('\n', ' ').split(' ') if y != ''] for x in input]
marks = [[0 for _ in x] for x in boards]
W = 5
tests = [
    [1 if i%W == x else 0 for i in range(W*W)] for x in range(W)
] + [
    [1 if i//W == x else 0 for i in range(W*W)] for x in range(W)
] + [
    [1 if i%W == i//W else 0 for i in range(W*W)],
    [1 if (W - 1 - i%W) == i//W else 0 for i in range(W*W)]
]
won: Set[int] = set()
score = None
for n in draw:
    for b in range(len(boards)):
        if b in won:
            continue
        if n in boards[b]:
            board = boards[b]
            mark = marks[b]
            mark[board.index(n)] = 1
            if any( sum( t[i]*mark[i] for i in range(W*W) ) == W for t in tests ):
                won.add(b)
                score = sum(board[i] for i in range(W*W) if mark[i] == 0 ) * n 
print(score)

