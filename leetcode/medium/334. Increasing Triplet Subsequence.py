class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_num1, min_num2 = 2 ** 31, 2 ** 31

        for i, v in enumerate(nums):
            if v <= min_num1:
                min_num1 = v
            elif v <= min_num2:
                min_num2 = v
            else:
                return True

        return False
