input = open('input.txt').read().split()[1:]
res = 0;
for i in input : res += int(i)
print(res)