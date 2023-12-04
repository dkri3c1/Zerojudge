a=list(map(int,input().split()))
b=list(map(int,input().split()))
a1=list(map(int,input().split()))
b1=list(map(int,input().split()))
suma=0
sumb=0
suma1=0
sumb1=0
for i in a:
    suma+=i
for i in b:
    sumb+=i
for i in a1:
    suma1+=i
for i in b1:
    sumb1+=i
count=0

if suma>sumb :
    count+=1
if suma1>sumb1:
    count+=1
if count == 2:
    print(f'{suma}:{sumb}')
    print(f'{suma1}:{sumb1}')
    print('Win')
elif count ==1:
    print(f'{suma}:{sumb}')
    print(f'{suma1}:{sumb1}')
    print('Tie')
else:
    print(f'{suma}:{sumb}')
    print(f'{suma1}:{sumb1}')
    print('Lose')