input = open('input.txt').read().split('\n')[1:]
for line in input :
    line = list(map(lambda x: int(x), line.split(' ')))
    for i in line :
        if i < max(line) and i > min(line) :
            print (i, end=' ')
