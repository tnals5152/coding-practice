from collections import deque

move = ((-1, 0), (1, 0), (0, -1), (0, 1))

class Solution:
    def setDefault(self, grid: List[list[int]]):
        self.len_row = len(grid)
        self.len_column = len(grid[0])
        self.visited = [[False for _ in grid[0]] for _ in grid]
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        que = deque()
        que.append((0, 0))#row, column
        self.setDefault(grid)
        
        while que:
            row, column = que.popleft()
            if self.visited[row][column]:
                continue
            
            self.visited[row][column] = True
            # print(row, column)

            ok, nexts = self.next(row, column)                

            if ok:
                que.append((nexts[0], nexts[1]))

            if grid[row][column] == 0:
                    continue

            for x, y in move:

                if not self.check(y, x, row, column):
                    count += 1
                    continue

                if grid[row + y][column + x] == 0:
                    count += 1

                if self.visited[row + y][column + x]:
                    continue

                que.append((row + y, column + x))

                
        return count
                
    def next(self, row, column):
        column += 1
        
        if column >= self.len_column:
            column = 0
            row += 1
        
        if row >= self.len_row:
            return False, [0, 0]
        
        return True, [row, column]  
                    
    def check(self, y, x, row, column) -> bool:
        if y + row < 0 or y + row >= self.len_row:
            return False
        
        if x + column < 0 or x + column >= self.len_column:
            return False
        
        return True
