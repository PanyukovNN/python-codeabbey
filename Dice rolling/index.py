import math
input = open('input.txt').read().split('\n')
for line in input[1:]:
    print(str(math.floor(float(line) * 6 + 1)), end = ' ')