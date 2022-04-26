class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_count = [0] * 3#[red, white, blue]
        
        for color in nums:
            color_count[color] += 1
        index = 0
        i = 0
        
        color_count = [[idx, v] for idx, v in enumerate(color_count) if v != 0]

        for i in range(len(nums)):
            if color_count[index][1] <= 0:
                index += 1
            
            nums[i] = color_count[index][0]
            color_count[index][1] -= 1
        
        
        
#         두번째 방법
#         color_count = [0] * 3#[red, white, blue]
        
#         for color in nums:
#             color_count[color] += 1
#         index = 0
#         i = 0

#         while i < len(nums):
#             if color_count[index] <= 0:
#                 index += 1
#                 continue
#             nums[i] = index
#             color_count[index] -= 1
#             i += 1

        
        # 첫번째 방법
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] > nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]
        
