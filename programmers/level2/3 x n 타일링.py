def solution(n):
    answer = 0
    if n % 2 != 0:
        return 0
    
    
    find_dict = dict()
    find_dict[2] = 3
    find_dict[4] = 11
    
    find_number = 6
    
    while find_number <= n:
        find_dict[find_number] = find_dict[find_number - 2] * 4 - find_dict[find_number - 4]
        find_number += 2
        
    return find_dict[n] % 1000000007
        
    
    
    
    
"""6, 41
8, 153
10, 571
12, 2131
14, 7953
"""

def find(n):
    # 시간초과 및 런타임 에러 코드
    if n <= 1:
        return 0
    if n == 2:
        return 3
    if n == 4:
        return 11
    
    
    return (find(n - 2) * 4 - find(n - 4)) % 1000000007
