class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = dict()
        
        for al in s:
            if s_dict.get(al) is None:
                s_dict[al] = 0
            s_dict[al] += 1
        
        for al in t:
            if not s_dict.get(al):
                return al
            s_dict[al] -= 1
            if s_dict[al] == 0:
                del s_dict[al]
                
        return ""
        
