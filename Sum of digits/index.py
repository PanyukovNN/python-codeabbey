input = open('input.txt').read().split('\n')[1:]
for line in input :
    line = list(map(lambda x: int(x), line.split(' ')))
    tmp = str(line[0] * line[0] + line[0])
    res = 0
    for i in tmp:
        res += int(i)
    print (res,end=' ')
