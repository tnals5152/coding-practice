class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.lower()
        title_list = title.split()
        
        for index, s in enumerate(title_list):
            if len(s) <= 2:
                continue
            title_list[index] = s[0].upper() + s[1:]
            
        return " ".join(title_list)
        
