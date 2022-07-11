move = ((-1, 0), (1, 0), (0, -1), (0, 1))
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        r_position = [0, 0]#(x, y)
        count = 0
        
        for y, xs in enumerate(board):
            found = False
            for x, value in enumerate(xs):
                if value == "R":
                    r_position = [x, y]
                    break
            if found:
                break
        
        for x, y in move:
            move_x, move_y = r_position[0] + x, r_position[1] + y
            
            while move_x >= 0 and move_x < len(board[0]) and move_y >= 0 and move_y < len(board):

                if board[move_y][move_x] == "p":
                    count += 1
                    break
                elif board[move_y][move_x] != ".":
                    break
                    
                move_x += x
                move_y += y
            
            
        return count
                    
                    
