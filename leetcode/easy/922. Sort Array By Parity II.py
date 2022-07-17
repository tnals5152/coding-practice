class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        num_list = []
        for a, b in zip([n for n in nums if n % 2 == 0], [n for n in nums if n % 2 == 1]):
            num_list.extend([a, b])
        return num_list
