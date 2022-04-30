class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted([[interval, i] for i, interval in enumerate(intervals)], key=lambda x: (x[0][0], x[0][1]))
        result = [intervals[0]]
        
        for i, interval in enumerate(intervals[1:]):#index = i + 1
            if interval[0][0] <= result[-1][0][1]:
                result[-1][0][1] = max(interval[0][1], result[-1][0][1])
            else:
                result.append(interval)

        return sorted([interval[0] for interval in result], key=lambda x: x[1])
