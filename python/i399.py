a,b,c=map(int,input().split())

large=max(a,b,c)
small=min(a,b,c)
mid=a+b+c-(large+small)

if large == small:
    print(3,large)
elif small == mid or large == mid:
    print(2,large,mid)
else:
    print(1,large,mid,small)