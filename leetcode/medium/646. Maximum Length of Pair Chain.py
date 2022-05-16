class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:(x[1], x[0]))
        count = 1
        before_index = 0
        index = 1
        
        while index < len(pairs):
            if pairs[before_index][1] < pairs[index][0]:
                count += 1
                before_index = index
            index += 1
        
        return count
                
