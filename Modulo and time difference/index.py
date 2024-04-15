input = open('input.txt').read().split('\n')[1:]
for line in input:
    d1, h1, m1, s1, d2, h2, m2, s2 = [int(x) for x in line.split()]
    dif = (d2 * 60 * 60 * 24 + h2 * 60 * 60 + m2 * 60 + s2) - (d1 * 60 * 60 * 24 + h1 * 60 * 60 + m1 * 60 + s1)
    d = dif//(60*60*24)
    dif -= d * 60 * 60 * 24
    h = dif // (60*60)
    dif -= h * 60 * 60
    m = dif // 60
    dif -= m * 60
    s = dif
    print ('({} {} {} {})'.format(d, h, m, s), end = ' ')