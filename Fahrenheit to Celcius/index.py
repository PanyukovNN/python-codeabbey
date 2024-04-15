input = open('input.txt').read().split(' ')[1:]
answer = ""
for el in input : answer += str(round(5/9 * (float(el) - 32))) + " "
print (answer)
