input = open('input.txt').read().split('\n')[1:]
for line in input:
    a = [int(x) for x in line.split(' ')]
    print(str(round(sum(a)/(len(a)-1))), end = ' ')