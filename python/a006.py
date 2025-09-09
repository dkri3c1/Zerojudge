a,b,c = map(int,input().split())

if b*b - 4 * (a*c) > 0  :
    s1 = int((-b + (b*b-(4*a*c))**0.5) // (2*a))
    s2 = int((-b - (b*b-(4*a*c))**0.5) // (2*a))
    big = max(s1,s2)
    small = min(s1,s2)
    print(f"Two different roots x1={big} , x2={small}")
elif b*b - 4* (a*c) == 0:
    s1 = int((-b + (b*b-(4*a*c))**0.5) // (2*a))
    print(f"Two same roots x={s1}")
else:
    print("No real root")