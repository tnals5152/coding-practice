from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_dict = Counter(s)
        
        for index, string in enumerate(s):
            if count_dict[string] == 1:
                return index
        return -1
        
