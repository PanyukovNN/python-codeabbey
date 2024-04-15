input = open('input.txt').read().split(' ')
for i in range(len(input)) : input[i] = int(input[i])
print (max(input), min(input))


