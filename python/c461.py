while True:
    try:
        a,b,c=map(int,input().split())
        if a!=0:
            a=1
        if b!=0:
            b=1
        if c==0:
            c=False
        else:
            c=True
        tmp=False
        if (a and b) == c:
            print('AND')
            tmp=True
        if (a or b) == c:
            print('OR')
            tmp=True
        if (a^b) == c:
            print('XOR')
            tmp=True
        if not tmp:
            print('IMPOSSIBLE')
    except:
        break