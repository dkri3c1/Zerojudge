'''
n,m=map(int,input().split())
for i in range(n,m):
'''
'''
n=input()
l=len(n)
sum=0
for i in n:
    sum += int(i)**l
    if sum == int(n):
        print(int(n))
'''
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

