class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_R = 0
        count_L = 0
        count = 0

        for string in s:
            if string == "R":
                count_R += 1
            else:
                count_L += 1

            if count_R == count_L:
                count += 1
                count_R = 0
                count_L = 0

        return count
