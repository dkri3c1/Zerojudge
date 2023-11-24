a,b,c=map(int,input().split())


test=b**2-(4*a*c)

if test>0:
    solve=int((-b+(b**2-4*a*c)**0.5)//2*a)
    solve2=int((-b-(b**2-4*a*c)**0.5)//2*a)
    print(f'Two different roots x1={solve} , x2={solve2}')
elif test == 0:
    solve=int((-b+(b**2-4*a*c)**0.5)//2*a)
    solve2=int((-b-(b**2-4*a*c)**0.5)//2*a)
    print(f'Two same roots x={solve2}')
elif test<0:
    print("No real root")