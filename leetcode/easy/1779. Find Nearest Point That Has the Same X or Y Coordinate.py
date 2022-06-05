class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index = [-1, -1]
        
        for idx, point in enumerate(points):
            if self.check_manhattan(x, y, point):
                index = self.change_index(index, point, x, y, idx)
                print(index)
                
        return index[1]
    
    def check_manhattan(self, x, y, point: List[int]):
        if (point[0] == x or point[1] == y):
            return True
        return False
    
    def change_index(self, index, point, x, y, idx):
        now_index = abs(point[0] - x) + abs(point[1] - y)
        
        
        if index[0] == -1 or now_index < index[0]:
            index = [now_index, idx]
            
        return index
