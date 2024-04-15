input = open('input.txt').read().split('\n')[1:]
for line in input :
    line = list(map(lambda x: int(x), line.split(' ')))
    if line[0] + line[1] >= line[2] and line[1] + line[2] >= line[0] and line[0] + line[2] >= line[1] : print ('1', end=' ')
    else: print ('0', end=' ')
