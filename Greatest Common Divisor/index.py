input = open('input.txt').read().split('\n')[1:]
for line in input:
    line = [int(x) for x in line.split()]
    i = 0
    while True:
        i += 1
        if line[0]%i == 0 and line[1]%i == 0 and i <= min(line):
            x = i
        if i % line[0] == 0 and i % line[1] == 0 and i >= max(line):
            print('({} {})'.format(x, i), end = ' ')
            break

