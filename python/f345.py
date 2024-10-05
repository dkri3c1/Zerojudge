n=int(input())
num=list(map(int,input().split()))
for i in range(len(num)-1,-1,-1):
    print(num[i],end=' ')