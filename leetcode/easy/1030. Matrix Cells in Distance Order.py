class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        distance_dict = dict()
        result = []
        
        for row in range(rows):
            for col in range(cols):
                key = abs(row - rCenter) + abs(col - cCenter)
                if distance_dict.get(key) is None:
                    distance_dict[key] = []
                distance_dict[key].append([row, col])
            
        for key in sorted(distance_dict.keys()):
            result.extend(distance_dict[key])
            
        return result
        