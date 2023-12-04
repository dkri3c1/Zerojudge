n=int(input())
number=list(map(int,input().split()))
number.sort()

min_score=101
max_score=-1

for j in range(len(number)):
    print(''.join(str(number[j])),end=' ')
print()
for i in number:
    if i<60:
        max_score=max(i,max_score)
    else:
        min_score=min(i,min_score)
if max_score == -1:
    print('best case')
else:
    print(max_score)
if min_score == 101:
    print('worst case')
else:
    print(min_score)