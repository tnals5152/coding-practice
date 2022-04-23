from collections import deque
class Solution:
    def __init__(self):
        self.visited = []
        self.grid_list = []
        self.move = ((-1, 0), (0, -1), (1, 0), (0, 1))
        
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid_list = grid
        self.visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        count = 0
        
        for x, v1 in enumerate(grid):
            for y, v2 in enumerate(v1):
                if v2 == "0" or self.visited[x][y]:
                    continue
                count += 1
                self.visit(x, y)
        return count
    
    def visit(self, a: int, b: int):
        que = deque()
        que.append((a, b))
        x_len = len(self.grid_list)
        y_len = len(self.grid_list[0])
        
        while que:
            a, b = que.popleft()
            
            for x, y in self.move:
                if a + x < 0 or a + x >= x_len or b + y < 0 or b + y >= y_len:
                    continue
                if self.grid_list[a + x][b + y] == "1" and\
                    not self.visited[a + x][b + y]:
                    self.visited[a + x][b + y] = True
                    que.append((a + x, b + y))
            
