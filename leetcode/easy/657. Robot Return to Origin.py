class Solution:
    def judgeCircle(self, moves: str) -> bool:
        position = [0, 0]
        move_dict = {
            "R": [1, 1],#position의 index, 움직이는 방향
            "L": [1, -1],
            "U": [0, 1],
            "D": [0, -1]
        }
        
        for move in moves:
            index, direction = move_dict[move]
            position[index] += direction
        
        if position == [0, 0]:
            return True
        return False
        
