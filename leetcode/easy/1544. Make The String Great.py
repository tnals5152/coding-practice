class Solution:
    def makeGood(self, s: str) -> str:
        index = 0
        s_list = list(s)
        
        while index < len(s_list) - 1:
            if s_list[index].lower() == s_list[index + 1].lower():#두 개가 같은 문자면
                if s_list[index] != s_list[index + 1]:
                    s_list = s_list[:index] + s_list[index + 2:]
                    if index > 0:
                        index -= 1
                    continue
            index += 1
        
        return "".join(s_list)
        
