n=int(input())
sum=0
number=list(map(int,input().split()))
if number[0] == 0:
    sum+=number[1]
if number[n-1]  == 0:
    sum+=number[n-2]
for i in range(1,n-1):
    if number[i] == 0:
        sum+=min(number[i-1],number[i+1])
print(sum)