input = open('input.txt').read().split('\n')[1:]
i = 0
answer = ""
for el in input :
    args = input[i].split(' ')
    answer += str(int(args[0]) + int(args[1])) + " "
    i+=1
print(answer)