move = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0)
}
max_point = 5
def solution(dirs):
    """
    move_dict = {
        [[0, 1], [1, 1]] : true, -> start_point, end_point
    }
    """
    move_set = set()
    answer = 0
    now_point = [0, 0]
    
    for s in dirs:
        move_point = [move[s][0] + now_point[0], move[s][1] + now_point[1]]
        if abs(move_point[0]) > 5 or abs(move_point[1]) > 5:#범위를 넘어가면 안 움직임
            continue
        
        move_set.add(((now_point[0], now_point[1]), (move_point[0], move_point[1])))
        move_set.add(((move_point[0], move_point[1]), (now_point[0], now_point[1])))
        now_point = move_point
    

    return len(move_set) // 2
    
    
    
    
    return answer
