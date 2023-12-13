n=int(input())
arr=[]
max_score=1000
mini_score=-1000
for i in range(n):
    x,y=map(int,input().split())
    arr.append([x,y])
for i in range(n-1):
    temp=abs(arr[i+1][0]-arr[i][0])+abs(arr[i+1][1]-arr[i][1])
    max_score=min(temp,max_score)
    mini_score=max(temp,mini_score)
print(mini_score,max_score)
