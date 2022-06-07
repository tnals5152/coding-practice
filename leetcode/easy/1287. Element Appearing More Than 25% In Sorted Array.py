class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        more_25 = len(arr) // 4
        count = 1
        
        for index in range(1, len(arr)):
            if arr[index - 1] == arr[index]:
                count += 1
                if count > more_25:
                    return arr[index]
            else:
                count = 1
                
        return arr[0]
