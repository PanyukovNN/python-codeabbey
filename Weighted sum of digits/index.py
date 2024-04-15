input = open('input.txt').read().split('\n')[1].split(' ')
for el in input :
    res = 0
    for i in range(len(el)) :
        res += (i+1) * int(el[i])
    print (res, end = ' ')
