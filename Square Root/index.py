input = open('input.txt').read().split('\n')[1:]
for line in input:
    X, N = [int(x) for x in line.split()]
    r = 1
    for i in range(N):
        r = (r + X/r)/2
    print (r, end=' ')



