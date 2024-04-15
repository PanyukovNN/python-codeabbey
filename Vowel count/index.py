vowels = 'aouiey'
answer = ""
input = open('input.txt').read().split('\n')[1:]
for line in input :
    Vcount = 0
    for i in line:
        if i in vowels : Vcount += 1
    answer += str(Vcount) + " "
print (answer)
