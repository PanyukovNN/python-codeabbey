input = open('input.txt').read().split(' ')[1:]
answer = ""
for el in input :
    args = el.split(' ')
    answer += str(round(float(args[0]) / float(args[1]))) + " "
print (answer)


