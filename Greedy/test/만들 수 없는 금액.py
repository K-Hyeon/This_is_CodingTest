n = input()
money = list(map(int,input().split()))

money.sort()

target = 1
for i in money:
    if target < i:
        break
    else: target += i
print(target)
