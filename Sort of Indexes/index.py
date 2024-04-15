input = [int(x) for x in open('input.txt').read().split('\n')[1].split()]
indexes = sorted(input)
for i in range(len(indexes)):
    print (input.index(indexes[i]) + 1, end = ' ')

