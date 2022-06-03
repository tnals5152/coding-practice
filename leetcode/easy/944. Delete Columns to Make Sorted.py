class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        
        for index in range(len(strs[0])):
            column_s = [s[index] for s in strs]
            if column_s == sorted(column_s):
                continue
            count += 1

        return count
