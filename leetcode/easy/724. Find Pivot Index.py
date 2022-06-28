class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        
        for index, n in enumerate(nums):
            right -= n

            if right == left:
                return index
            
            left += n
            
        return -1
        
        