n=int(input())
arr=[]
time=[]
wrong = 0
for i in range(n):
    x,y=map(int,input().split())
    arr.append(y)
    time.append(x)
    if y<0:
        wrong+=1
times=len(time)
ans=max(arr)-times-(wrong*2)
t=time[arr.index(max(arr))]
if ans<0:
    print(0,t)
else:
    print(ans,t)
