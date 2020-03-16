Alice = [int(x) for x in input().split()]
Bob = [int(y) for y in input().split()]
AlicePoints =0
BobPoints =0
for i in range(3):
    if Alice[i]>Bob[i]:
        AlicePoints+=1
    elif Alice[i]<Bob[i]:
        BobPoints+=1
    else:
        pass
print(f'{AlicePoints} {BobPoints}')