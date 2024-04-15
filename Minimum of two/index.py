input = open('input.txt').read().split('\n')[1:]
answer = ""
for el in input :
    args = el.split(' ')
    if int(args[0]) > int(args[1]) : answer += args[1] + " "
    else: answer += args[0] + " "
print(answer)

