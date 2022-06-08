class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        now_num = n - 1
        
        for num in range(now_num, 0, -1):
            if "0" in str(num) or "0" in str(n - num):
                continue
            return [num, n - num]
