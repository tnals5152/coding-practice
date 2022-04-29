from collections import deque
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        visited_count = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        x_len = len(grid[0])
        y_len = len(grid)
        
        for y in range(y_len):
            for x in range(x_len):
                visited_count[y][x] = grid[y][x]
                if x == 0 and y == 0:#초기면 그대로 값 더함
                    # visited_count[y][x] = grid[y][x]
                    continue
                elif y == 0:#첫번째 줄이면 이전 값들로 더함
                    visited_count[y][x] += visited_count[y][x - 1]
                elif x == 0:#첫번째 라인이면 위의 값들을 더함
                    visited_count[y][x] += visited_count[y - 1][x]
                else:
                    visited_count[y][x] += min(visited_count[y - 1][x], visited_count[y][x - 1])

        return visited_count[-1][-1]
        
        

        
#         첫번째 방법(시간 초과)
#         move = ((0, 1), (1, 0))
#         visited_count = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
#         que = deque()
#         que.append((0, 0, 0))#x, y, total
        
#         while que:
#             x, y, total = que.popleft()
            
#             if x >= len(grid[0]) or y >= len(grid):
#                 continue
#             # print(x, y)
#             if visited_count[y][x] != 0 and visited_count[y][x] <= total + grid[y][x]:
#                 continue
            
#             visited_count[y][x] = total + grid[y][x]
#             total = visited_count[y][x]
            
#             for position in move:
#                 que.append((x + position[0], y + position[1], total))
        
#         # print(visited_count)
#         return visited_count[-1][-1]
