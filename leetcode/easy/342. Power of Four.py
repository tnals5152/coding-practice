class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        while n > 0:
            n2 = n / 4
            if not n2.is_integer() and n2 >= 1:
                return False
            n2 = int(n2)
            if (n2 == 1 and n % 4 == 0) or (n2 == 0 and n % 4 == 1):
                return True
            n = n2
        return False
            
