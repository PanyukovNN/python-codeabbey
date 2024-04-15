a = [int(x) for x in open('input.txt').read().split('\n')[1].split()]
for el in a:
    i = 0
    while el != 1:
        i += 1
        if el % 2 == 0: el /= 2
        else: el = 3 * el + 1
    print (i, end = ' ')
