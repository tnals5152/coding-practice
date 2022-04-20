class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        result = "".join(sorted([str(v) for v in nums], key=NumKey))
        if int(result) == 0:
            return "0"
        return result
    

#key비교를 앞 뒤를 비교하고 싶을 땐 class의 __lt__메소드 이용!
class NumKey(str):
    def __lt__(a, b):
        return a + b > b + a
