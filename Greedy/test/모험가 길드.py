n = int(input())
horreur = list(map(int, input().split()))

horreur.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in horreur: # 공포도가 낮은 것부터 확인
    count += 1 # 현재 그룹에 해당 모험가 포함시킴
    if count >= i:
        result += 1
        count = 0 # 그룹에 포함된 모험가 수 초기화
        
print(result)
