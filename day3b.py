input = open('day3.txt').readlines()
width = len(input[0].strip())
numbers = [int(l, 2) for l in input]
def calc(invert: bool):
    list = [*numbers]
    for i in range(width):
        bitidx = width - 1 - i
        bit = 1 << bitidx
        condition = (sum(n & bit for n in list) >> bitidx) >= len(list)/2
        val = bit if condition ^ invert else 0
        list = [n for n in list if n & bit == val]
        if len(list) == 1:
            break
    return list[0]
print(calc(False) * calc(True))
