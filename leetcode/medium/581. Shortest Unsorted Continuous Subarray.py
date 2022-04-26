class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        check = False
        nums_sorted = sorted(nums)
        start = 0
        end = len(nums) - 1
        
        for i in range(len(nums)):
            if nums[i] != nums_sorted[i]:
                start = i
                check = True
                break
        
        if not check:
            return 0
        
        for i in range(len(nums) - 1, 0 - 1, -1):
            if nums[i] != nums_sorted[i]:
                end = i
                break
        
        return end - start + 1
        
        
        
#         첫번째 방법 틀림
#         max_val = nums[0]
#         check = True
#         start = 0
#         end = 0
        
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1] or nums[i] < max_val:#이전 값이 더 크거나, 지금까지 중의 가장 큰 값보다 현재 값이 작을 때
#                 if check:
#                     start = i
#                     end = i + 1
#                     check = False
#                 else:
#                     end = i
#                 max_val = max(max_val, nums[i])
        
#         if max_val > nums[-1]:
#             end = len(nums) - 1
#         print(start, end)
#         return end - start + 1 if start != end else 0
