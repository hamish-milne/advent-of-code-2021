from typing import List

cscores = [None, ')', ']', '}', '>']
pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
scores: List[int] = []
for line in open('day10.txt').readlines():
    stack: List[str] = []
    corrupt = False
    for c in line.strip():
        if c in pairs:
            stack.append(pairs[c])
        else:
            expected = stack.pop()
            if c != expected:
                corrupt = True
                break
    if not corrupt:
        score = 0
        stack.reverse()
        for c in stack:
            score = score*5 + cscores.index(c)
        scores.append(score)
scores.sort()
print(scores[len(scores) // 2])
