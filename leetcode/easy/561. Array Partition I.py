class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #1, 2, 2, 5, 6, 6
        nums.sort()
        total = 0
        
        for i in range(0, len(nums), 2):
            total += nums[i]
        
        return total
