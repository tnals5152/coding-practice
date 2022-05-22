class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)
        max_candies = max(candies)
                                    
        for i, candy in enumerate(candies):
            if candy + extraCandies >= max_candies:
                result[i] = True
                                                                                        
        return result
