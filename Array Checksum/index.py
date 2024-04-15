input = open('input.txt').read().split('\n')[1:]
a = [int(x) for x in input[0].split(' ')]
result = 0
for el in a:
    result = (result + el) * 113 % 10000007
print(result)
