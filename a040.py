ok=0
n,m=map(int,input().split())
for j in range(n,m):
    j=str(j)
    l=len(j)
    sum=0
    for k in j:
        sum += int(k)**l
    if sum == int(j):
        print(j,end=' ')
        ok=len(j)
if ok==0:
    print('none')

