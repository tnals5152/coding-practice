class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        
        for num in range(left, right + 1):
            if self.self_dividing(num):
                result.append(num)
                
        return result
                
                
    def self_dividing(self, num):
        str_num = str(num)
        
        for s_num in str_num:
            if s_num == "0":
                return False
            if num % int(s_num) != 0:
                return False
        
        return True
