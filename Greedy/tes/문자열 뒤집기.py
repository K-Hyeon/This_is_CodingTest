num = input()

count0 = 0
count1 = 0

if num[0] == '0':
    count0 += 1
else :
    count1 += 1
    
for i in range(0, len(num) - 1):
    if num[i] != num[i+1]:
        if num[i+1] == '1':
            count0 += 1
        else :
            count1 += 1
print(min(count0, count1))
