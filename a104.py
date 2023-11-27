while True:
    try:
        n=int(input())
        number=list(map(int,input().split()))
        for i in range(len(number)-1):
            for j in range(len(number)-i-1):
                if number[j] > number[j+1]:
                    number[j],number[j+1] = number[j+1],number[j]
        for b in number:
            print(b,end=' ')
        print()
    except:
        break