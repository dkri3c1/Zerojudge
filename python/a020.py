def create_dict():
    dic = {}
    for i in range(26):
        key = chr(ord('A')+i)
        dic[key] = 10+i
    return dic
#print(create_dict()) => {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
d_ans = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 34, 'J': 18, 'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31, 'Z': 33}

cipher = input()

letter_id = cipher[:1]
num_id = list(cipher[1:])

ten = int(d_ans[letter_id]) // 10
digit = int(d_ans[letter_id]) % 10

sum = ten

for n in range(8,0,-1):
    sum+=int(num_id[8-n])*n
sum += int(num_id[len(num_id)-1])

sum+=digit*9

if sum % 10 == 0:
    print("real")
else:
    print("fake")