class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_dict = dict()
        include_elements = []
        not_include_elements = []
        
        for num in arr2:
            arr2_dict[num] = 0
        
        
        for num in arr1:
            if arr2_dict.get(num) is not None:
                arr2_dict[num] += 1
            else:
                not_include_elements.append(num)
                
        for num in arr2:
            include_elements.extend([num] * arr2_dict[num])
            
        return include_elements + sorted(not_include_elements)
