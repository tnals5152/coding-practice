class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s_alphabet = []
        result_s = list(s)
        s_index = len(s_alphabet) - 1
        
        for value in s:
            if value.isalpha():
                s_alphabet.append(value)
        
        for i, value in enumerate(s):
            if value.isalpha():
                result_s[i] = s_alphabet[s_index]
                s_index -= 1
                
        
        return "".join(result_s)