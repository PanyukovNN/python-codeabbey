input = open('input.txt').read().split('\n')
result = int(input[0])
for line in input[1:-1]:
    if line.split()[0] == '+': result += int(line.split()[1])
    elif line.split()[0] == '*': result *= int(line.split()[1])
    result %= int(input[-1].split()[1])
print (result)
