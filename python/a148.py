while True:
    try:
        n=list(map(int,input().split()))
        sum=0
        total=0
        for i in range(1,len(n)):
            sum+=n[i]
        total=sum//n[0]
        if total >= 59:
            print('no')
        else:
            print('yes')
    except:
        break