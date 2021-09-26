n = int(input())
move = list(map(str, input().split()))

x = 1
y = 1

if move[0] == 'R':
    y += 1
elif move[0] == 'D':
    x += 1
    
for i in range(1, len(move)):
    if move[i] == 'R':
        if y < 5:
            y += 1
    elif move[i] == 'U':
        if x > 1:
            x -= 1
    elif move[i] == 'L':
        if y > 1:
            y -= 1
    elif move[i] == 'D':
        if x < 4:
            x += 1
            
print(x, " ",y)
