class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1 + nums2)
        nums2_set = set(nums1 + nums2)
        
        for num in set(nums2):
            nums1_set.remove(num)
        
        for num in set(nums1):
            nums2_set.remove(num)
            
        return [list(nums1_set), list(nums2_set)]
