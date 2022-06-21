class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        """
        [
            [3,0,8,4],
            [2,4,5,7],
            [9,2,6,3],
            [0,3,1,0]
        ]
        """
        
        result = 0
        column_grid = [-1 for _ in range(len(grid[0]))]#가로
        row_grid = [-1 for _ in range(len(grid))]#세로
        
        for row_index, row_value in enumerate(grid):
            for column_index, column_value in enumerate(row_value):
                if row_grid[column_index] == -1:
                    row_grid[column_index] = max([v[column_index] for v in grid])
                if column_grid[row_index] == -1:
                    column_grid[row_index] = max(row_value)
                
                result += min(row_grid[column_index], column_grid[row_index]) - grid[row_index][column_index]

        
        return result
