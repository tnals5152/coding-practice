class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for num, i in zip(nums, index):
            if len(result) <= i:
                result.append(num)
            else:
                result = result[:i] + [num] + result[i:]
        return result
                                                                                                                
