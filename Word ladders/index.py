input = [x.split() for x in open('input.txt')]
raws = [x[:-1:] for x in open('words.txt')]

for step in input[1:]:
    a = step[0]
    b = step[1]

    words = []
    for i in raws:
        if len(i) == 5:
            words.append(i)

    Mass = [a]
    def findVariants(a):
        tmp = []
        for el in words:
            l = 0
            for i in range(5):
                if a[i] != el[i]:
                    l += 1
                if l > 1:
                    break
            if l == 1:
                tmp.append(el)
        for i in tmp:
            words.remove(i)
        return(tmp)

    def NewMass(Mass):
        tmpMass = []
        for i in Mass:
            tmp = findVariants(i)
            for el in tmp:
                tmpMass.append(el)
        return(tmpMass)

    val = 1
    while b not in Mass:
        Mass = NewMass(Mass)
        val += 1

    print(val)
