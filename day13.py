[t_dots, t_folds] = open('day13.txt').read().split("\n\n")
dots = [[int(x) for x in y.split(',')] for y in t_dots.splitlines(keepends=False)]
for fold in t_folds.splitlines(keepends=False):
    [t_axis, t_position] = fold.split('=')
    position = int(t_position)
    axis = 1 if t_axis.endswith('y') else 0
    for dot in dots:
        if dot[axis] > position:
            dot[axis] = 2*position - dot[axis]
    print(len(set(tuple(dot) for dot in dots)))
    exit()
