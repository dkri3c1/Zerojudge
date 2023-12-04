A1,B1,C1=map(int,input().split())
A2,B2,C2=map(int,input().split())
n=int(input())

C=-1

for i in range(n+1):
    x1=i
    y1=A1*x1**2+(B1*x1)+C1
    x2=n-x1
    y2=A2*x2**2+(B2*x2)+C2
    biggest=(max(C,(y1+y2)))
print(biggest)