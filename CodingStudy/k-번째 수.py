n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
arr = [[i*j for j in range(1, n+1)] for i in range(1, n+1)]

arr2 = []
for i in range(n):
    for j in range(n):
        arr2.append(arr[i][j])

arr2.sort()

print(arr2[k])
