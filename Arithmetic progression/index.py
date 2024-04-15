input = open('input.txt').read().split('\n')[1:]
for line in input:
    line = list(map(lambda x: int(x), line.split(' ')))
    res = 0
    for i in range(line[2]) :
        res += line[0] + line[1] * i
    print (res, end=' ')
