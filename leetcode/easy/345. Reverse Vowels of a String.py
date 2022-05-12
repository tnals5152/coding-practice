class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        start = "" if s[0].lower() not in vowels else s[0]
        end = "" if s[-1].lower() not in vowels else s[-1]
        start_index = 0
        end_index = len(s) - 1
        s = list(s)
        
        while start_index < end_index:
            if start == "":#start부터 맞추기
                if s[start_index].lower() in vowels:
                    start = s[start_index]
            elif end == "":#끝부분 맞추기
                if s[end_index].lower() in vowels:
                    end = s[end_index]
            
            if start != "" and end != "":
                s[start_index], s[end_index] = s[end_index], s[start_index]
                start, end = "", ""
                
            if start == "":
                start_index += 1
            elif end == "":
                end_index -= 1
        
        return "".join(s)
