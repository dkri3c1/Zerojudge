while True:
    try:
        n,m=map(int,input().split())
        a=0
        b=0
        while True:
            a+=1
            b+=n
            n+=1
            if b>m:
                print(a)
                break
    except:
        break