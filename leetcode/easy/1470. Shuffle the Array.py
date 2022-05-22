class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        width = len(nums) // 2

        for i in range(width):
            result.append(nums[i])
            result.append(nums[width + i])
        
        return result
