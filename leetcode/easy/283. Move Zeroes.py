class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, end = 0, len(nums)
        while i < end:
            if nums[i] == 0:
                nums[i:] = nums[i + 1:] + [0]
                end -= 1
            else:
                i += 1
