input = open('input.txt').read().split('\n')[1:]
answer = ""
for el in input :
    args = el.split(' ')
    if int(args[0]) <= int(args[1]) and int(args[0]) <= int(args[2]) : answer += args[0] + " "
    elif  int(args[1]) <= int(args[0]) and int(args[1]) <= int(args[2]) : answer += args[1] + " "
    else: answer += args[2] + " "
print(answer)

