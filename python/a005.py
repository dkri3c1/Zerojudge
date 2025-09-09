n = int(input())
for i in range(n):
    l = list(map(int,input().split()))
    if l[3] - l[2] == l[2] - l[1]:
        l.append(l[3]+l[3]-l[2])
        print(' '.join(map(str,l)))
    else:
        l.append(l[3]*(l[3]//l[2]))
        print(' '.join(map(str,l)))