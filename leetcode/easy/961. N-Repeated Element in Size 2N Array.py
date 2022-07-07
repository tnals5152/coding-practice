from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count_dict = Counter(nums)
        
        for key, value in count_dict.items():
            if value == len(nums) // 2:
                return key
            
        return 0
