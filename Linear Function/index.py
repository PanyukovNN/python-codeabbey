input = open('input.txt').read().split('\n')[1:]
for line in input:
    x1, y1, x2, y2 = [int(x) for x in line.split()]
    a = (y2 - y1)//(x2 - x1)
    b = y1 - a * x1
    print('({0} {1})'.format(a, b), end = ' ')