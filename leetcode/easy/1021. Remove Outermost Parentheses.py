class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        
        start = 0
        end = 0
        
        for index, string in enumerate(s):
            if string == '(':
                start += 1
            else:
                end += 1

            if start == end:
                result += s[index - start * 2 + 2:index]
                start, end = 0, 0
                
        return result
        
