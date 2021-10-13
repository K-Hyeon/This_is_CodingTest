def solution(orders, course):
    from itertools import combinations
    answer = []
    for i in course:
        temp = []
        for menu in orders:
            m = sorted(list(menu))
            for c in combinations(m, i):
                temp.append("".join(c))
        count={}
        for i in temp:
            try: count[i] += 1
            except: count[i]=1

        d = [k for k, v in count.items() if max(count.values()) > 1 and max(count.values()) == v]
        for i in d: answer.append(i)

    return sorted(answer)
