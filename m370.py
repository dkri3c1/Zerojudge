x,n=map(int,input().split())
b=list(map(int,input().split()))

count=0
count2=0
for i in range(len(b)):
    if x<b[i]:
        count+=1
    else:
        count2+=1
if count>count2:
    print(count)
    print(max(b))
else:
    print(count2)
    print(min(b))