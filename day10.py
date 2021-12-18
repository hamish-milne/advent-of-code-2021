from typing import List

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
score = 0
for line in open('day10.txt').readlines():
    stack: List[str] = []
    for c in line.strip():
        if c in pairs:
            stack.append(pairs[c])
        else:
            expected = stack.pop()
            if c != expected:
                score += scores[c]
                break
print(score)
