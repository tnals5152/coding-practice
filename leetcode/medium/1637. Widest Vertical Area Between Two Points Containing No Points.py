class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        before = points[0][0]
        result = 0
        
        for point in points[1:]:
            result = max(result, point[0] - before)
            before = point[0]
            
        return result
        
