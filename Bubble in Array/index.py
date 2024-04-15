input = [int(x) for x in open('input.txt').read().split()[:-1]]
swaps = 0
for i in range(1, len(input)):
    if input[i-1] > input[i]:
        input.insert(i-1, input.pop(i))
        swaps += 1
checksum = 0
for el in input:
    checksum = (checksum + el) * 113 % 10000007
print (swaps, checksum)

