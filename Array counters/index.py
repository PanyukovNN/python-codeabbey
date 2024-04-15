input = open('input.txt').read().split('\n')
count = [0] * int(input[0].split()[1])
for el in input[1].split():
    count[int(el)-1] += 1
print(' '.join(str (x) for x in count))