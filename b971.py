while True:
    try:
        n=list(map(int,input().split()))
        a1=n[0]
        an=n[1]
        d =n[2]
        for i in range(a1,an+1,d):
            print(i,end=' ')
    except:
        break
