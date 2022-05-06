from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        que = deque()
        
        move = ((-1, 0), (0, -1), (1, 0), (0, 1))
        # que.append((x, y))
        
        for y in range(len(board)):
            que.append((y, 0))
            if len(board[y]) == 1:
                continue
            que.append((y, len(board[y]) - 1))
            if y == 0 or y == len(board) - 1:
                for i in range(1, len(board[y]) - 1):
                    que.append((y, i))

        
        while que:
            y, x = que.popleft()

            if board[y][x] == "O":
                board[y][x] = "S"
            else:
                continue
            
            for  a, b in move:
                if a + y >= len(board) or a + y < 0 or\
                    b + x >= len(board[0]) or b + x < 0:
                    continue
                que.append((a + y, b + x))
        
        
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == "O":
                    board[y][x] = "X"
                elif board[y][x] == "S":
                    board[y][x] = "O"
        
        
