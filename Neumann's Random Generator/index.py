input = [x for x in open('input.txt').read().split('\n')[1].split(' ')]
for i in range(len(input)):
    arr = [input[i]]
    while arr.index(arr[-1]) == len(arr)-1:
        input[i] = str(pow(int(input[i]),2))
        input[i] = ('0' *  (8 - len(input[i])) + input[i])[2:6]
        arr.append(input[i])
    print(len(arr)-1, end = ' ')


