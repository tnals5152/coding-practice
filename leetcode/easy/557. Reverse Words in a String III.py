class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        
        for index, v in enumerate(s_list):
            s_list[index] = v[::-1]
            
        
        return " ".join(s_list)
        
