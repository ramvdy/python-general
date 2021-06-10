i = 0

fiblist = [0,1]

while len(fiblist) < 10:
    fiblist.append(fiblist[i]+fiblist[i+1])
    i+=1

print(len(fiblist))
print(fiblist)