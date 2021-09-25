data = list(map(int,input()))

s = len(data)
s_2 = int(s / 2)
result = 0

for i in range (s_2):
    result += data[i]

for i in range (s_2, s):
    result -= data[i]
    
if result == 0:
    print("LUCKY")
else :
    print("READY")
