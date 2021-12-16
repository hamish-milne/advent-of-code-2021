input = [ ord(c)-(ord('A')-10 if c >= 'A' else ord('0')) for c in open('day16.txt').read() if not c.isspace() ]
input.reverse()
bbuf = 0
bcount = 0
rcount = 0
def shift(count: int):
    global bbuf
    global bcount
    global rcount
    out = 0
    while count > 0:
        if bcount == 0:
            bcount = 4
            bbuf = input.pop()
        bcount -= 1
        count -= 1
        rcount += 1
        out <<= 1
        out |= (bbuf & (1 << bcount)) >> bcount
    return out

total = 0
def packet():
    global total
    version = shift(3)
    total += version
    type = shift(3)
    if type == 4:
        literal = 0
        nibble = 0b10000
        while nibble >= 0b10000:
            nibble = shift(5)
            literal <<= 4
            literal |= nibble & 0b1111
    else:
        if shift(1):
            subpackets = shift(11)
            for _ in range(subpackets):
                packet()
        else:
            length = shift(15)
            end_at = rcount + length
            while rcount < end_at:
                packet()

packet()
print(total)
