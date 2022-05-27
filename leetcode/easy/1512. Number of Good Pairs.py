class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        num_dict = dict()
        """
        num_dict = {
            1: 3,  #number : count
            2: 1,
            3: 2
        }
        """
        
        for num in nums:
            if not num_dict.get(num):
                num_dict[num] = 0
            num_dict[num] += 1
        
        for _, value in num_dict.items():
            if value > 1:
                count += self.add_count(value)
                
        return count
    
    def add_count(self, value):
        return int(self.factorial(value)//(self.factorial(value - 2) * 2))
        
        
    def factorial(self, number):
        if number <= 1:
            return 1
        return number * self.factorial(number - 1)
