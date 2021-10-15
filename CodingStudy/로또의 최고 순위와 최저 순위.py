def solution(lottos, win_nums):
    accord_num = [n for n in lottos if n in win_nums]
    nc_num = lottos.count(0)
    rank = [6,6,5,4,3,2,1]
            
    max_accord = len(accord_num) + nc_num
    min_accord = len(accord_num)
    answer = [rank[max_accord], rank[min_accord]] 

    return answer
