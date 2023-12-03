n=input()

arr=[]

k=[]
c=[]
for i in n:
    arr.append(int(i))

for i in range(len(arr)):
    if i%2==0:
        k.append(arr[i])
    else:
        c.append(arr[i])
A=0
B=0
for i in range(len(k)):
    A+=k[i]
for i in range(len(c)):
    B+=c[i]
print(abs(A-B))
