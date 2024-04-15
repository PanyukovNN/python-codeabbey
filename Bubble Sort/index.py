input = [int(x) for x in open('input.txt').read().split('\n')[1].split()]
count = [0, 0]
while True:
    stop = True
    for i in range(0, len(input)-1):
        if input[i] > input[i+1]:
            input.insert(i+1, input.pop(i))
            count[1] += 1
            stop = False
    count[0] += 1
    if stop == True: break
print (count[0], count[1])
