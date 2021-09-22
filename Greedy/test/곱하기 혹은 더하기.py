num = input()
result = int(num[0])

for i in range(1, len(num)):
    assist = int(num[i])
    if assist < 1 or result < 1:
        result += assist
    else :
        result *= assist
print(result)
