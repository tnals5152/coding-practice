class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_dict = dict()
        result = 0
        
        for stone in stones:
            if stones_dict.get(stone) is None:
                stones_dict[stone] = 0
            stones_dict[stone] += 1
        
        for jewel in jewels:
            if stones_dict.get(jewel):
                result += stones_dict.get(jewel)
        
        return result
