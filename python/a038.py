#print(''.join(reversed(input())))
while True:
    try:
        a=list(input())
        b=a[::-1]
        output=''.join(b)
        print(int(output))
    except:
        break