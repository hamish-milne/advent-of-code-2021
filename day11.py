text = open('day11.txt').read()
size = text.index('\n')
octopus = [ int(c) for c in text if c.isdigit() ]
flashed = [False]*len(octopus)
flash_count = 0
for _ in range(100):
    for i in range(len(octopus)):
        if flashed[i]:
            flashed[i] = False
            octopus[i] = 0
        octopus[i] += 1
    continue_flash = True
    while continue_flash:
        continue_flash = False
        for i in range(len(octopus)):
            if octopus[i] > 9 and not flashed[i]:
                flash_count += 1
                flashed[i] = True
                continue_flash = True
                edge_l = (i%size) > 0
                edge_r = (i%size) < (size-1)
                edge_t = (i//size) > 0
                edge_b = (i//size) < (size-1)
                if edge_l:
                    octopus[i - 1] += 1
                if edge_r:
                    octopus[i + 1] += 1
                if edge_t:
                    octopus[i - size] += 1
                if edge_b:
                    octopus[i + size] += 1
                if edge_l and edge_t:
                    octopus[i - 1 - size] += 1
                if edge_l and edge_b:
                    octopus[i - 1 + size] += 1
                if edge_r and edge_t:
                    octopus[i + 1 - size] += 1
                if edge_r and edge_b:
                    octopus[i + 1 + size] += 1
print(flash_count)
