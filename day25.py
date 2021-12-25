
states = ['.', '>', 'v']
grid = [ [states.index(c) for c in line if c in states] for line in open('day25.txt').readlines() ]

step = 0
moving = True
while moving:
    step += 1
    moving = False
    grid2 = [ [0]*len(row) for row in grid ]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 2:
                grid2[y][x] = 2
                continue
            if grid[y][x] != 1:
                continue
            dst = (x+1)%len(grid[y])
            if grid[y][dst] == 0:
                grid2[y][dst] = 1
                moving = True
            else:
                grid2[y][x] = 1
    grid = grid2
    grid2 = [ [0]*len(row) for row in grid ]

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                grid2[y][x] = 1
                continue
            if grid[y][x] != 2:
                continue
            dst = (y+1)%len(grid)
            if grid[dst][x] == 0:
                grid2[dst][x] = 2
                moving = True
            else:
                grid2[y][x] = 2
    grid = grid2

    # for row in grid:
    #     for c in row:
    #         print(states[c], end='', flush=False)
    #     print('')
    # print('')
print(step)