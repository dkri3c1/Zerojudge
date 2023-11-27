n=int(input())
if n<=10:
    print(n*6)
elif n>10 and n<=20:
    print(60+((n-10)*2))
elif n>20 and n<=40:
    print(80+((n-20)*1))
elif n==0:
    print(0)
else:
    print(100)