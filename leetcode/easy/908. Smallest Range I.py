class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_num = min(nums)
        max_num = max(nums)
        k_range = 2 * k
        
        return max(0, max_num - min_num - k_range)