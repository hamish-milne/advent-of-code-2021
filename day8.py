input = [[y.strip() for y in x.split(' ')] for x in open('day8.txt').readlines()]
lengths = (2, 3, 4, 7)
print ( sum( sum(1 if len(x[i]) in lengths else 0 for i in range(11, 15)) for x in input))
