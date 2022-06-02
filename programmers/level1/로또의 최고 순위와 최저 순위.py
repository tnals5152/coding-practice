def solution(lottos, win_nums):
    rank = {
        6: 1,
        5: 2,
        4: 3,
        3: 4, 
        2: 5,
        1: 6,
        0: 6
    }
    win_dict = dict()
    count = 0
    miss_count = 0
    
    for win_num in win_nums:
        win_dict[win_num] = True
    
    for lotto in lottos:
        if lotto == 0:
            miss_count += 1
            continue
        
        if win_dict.get(lotto):
            count += 1
            
    return [rank[count + miss_count], rank[count]]
    
    
    
    
    #이전 풀이
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    count = 0
    
    for element in lottos:
        if element in win_nums:
            count += 1
    
    answer.append(rank[count + lottos.count(0)])
    answer.append(rank[count])
    
    return answer
