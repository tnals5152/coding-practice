from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_dict = Counter(nums)
        keys_list = sorted(nums_dict.keys())
        max_count = 0
        for i, key in enumerate(keys_list[:-1]):
            next_key = keys_list[i + 1]
            if key + 1 == next_key:
                max_count = max(max_count, nums_dict[key] + nums_dict[next_key])

        return max_count
