class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = []
        
        for num in nums:
            if num % 2 == 0:
                result.insert(0, num)
            else:
                result.append(num)
                
        return result
        
        
        
#         첫번째 방법
#         odd = []
#         even = []
        
#         for num in nums:
#             if num % 2 == 0:
#                 even.append(num)
#             else:
#                 odd.append(num)
        
#         return even + odd
