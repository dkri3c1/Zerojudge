n,d=map(int,input().split())
count=0
sum=0
for i in range(n):
    a,b,c=map(int,input().split())
    if max(a,b,c) - min(a,b,c) >=d:
        count+=1
        sum+=int((a+b+c)//3)
print(count,sum)