class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        
        for query in queries:
            count = 0
            for point in points:
                if (point[0] - query[0]) ** 2 + (point[1] - query[1]) ** 2 <= query[2] ** 2:
                    count += 1
            result.append(count)
            
        return result
