class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_n = 1
        sum_n = 0
        
        while n > 0:
            number = n % 10
            n = n // 10
            product_n *= number
            sum_n += number
            
        return product_n - sum_n
            
