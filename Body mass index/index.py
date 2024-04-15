input = open('input.txt').read().split('\n')[1:]
for line in input:
    line = list(map(lambda x: float(x), line.split(' ')))
    BMI = line[0] / (line[1]*line[1])
    if BMI < 18.5 : print ('under', end=' ')
    elif BMI < 25 and BMI >= 18.5 : print ('normal', end=' ')
    elif BMI < 30 and BMI >= 25 : print ('over', end=' ')
    elif BMI >= 30 : print ('obese', end=' ')
