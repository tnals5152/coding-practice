class Solution:
    def reverseStr(self, s: str, k: int) -> str:
    
        for index in range(0, len(s), 2 * k):
            s = s[:index] + s[index:index + k][::-1] + s[index + k:]
            
        return s
