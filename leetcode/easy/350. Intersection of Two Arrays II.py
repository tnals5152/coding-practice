class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_count = dict()
        result = []
        
        for num in nums1:
            if nums1_count.get(num):
                nums1_count[num] += 1
            else:
                nums1_count[num] = 1
        
        for num in nums2:
            if nums1_count.get(num):
                result.append(num)
                if nums1_count[num] == 1:
                    del nums1_count[num]
                else:
                    nums1_count[num] -= 1
        
        return result
