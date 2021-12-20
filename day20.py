file = [[1 if c == '#' else 0 for c in line if not c.isspace()] for line in open('day20.txt').readlines()]

alg = file[0]
image = file[2:]
w = 3
pad = 0

def padimg():
    for row in image:
        row.insert(0, pad)
        row.append(pad)
    image.insert(0, [pad]*len(image[0]))
    image.append([pad]*len(image[0]))

padimg()
padimg()
for s in range(50):
    padimg()
    image2 = [[pad]*len(row) for row in image]

    pad = pad ^ alg[0]
    for y in range(len(image)):
        for x in range(len(image[y])):
            if y > 1 and y < len(image)-1 and x > 1 and x < len(image[y])-1:
                idx = 0
                for i in range(w*w):
                    idx <<= 1
                    idx |= image[(y-1)+(i//w)][(x-1)+(i%w)]
                image2[y][x] = alg[idx]
            else:
                image2[y][x] = pad

    # for row in image2:
    #     for p in row:
    #         print('#' if p == 1 else '.', end='', flush=False)
    #     print('')
    # print('')
    image = image2
print(sum(sum(row) for row in image))
