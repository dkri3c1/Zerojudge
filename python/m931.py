n=int(input())

arr=[]

arr_num=[]
for i in range(n):
    num=list(map(int,input().split()))
    temp=num[0]**2+num[1]**2
    arr.append(temp)
    arr_num.append(num)
arr.sort()

for j in range(len(arr)):
    if (arr_num[j][0]**2 + arr_num[j][1]**2) == arr[n-2]:
        print(arr_num[j][0],arr_num[j][1])

