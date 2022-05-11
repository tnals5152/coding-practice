class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_index_dict = dict()
        before_index = -1
        
        for i, v in enumerate(t):
            if t_index_dict.get(v):
                t_index_dict[v].append(i)
            else:
                t_index_dict[v] = [i]
                
        for i, v in enumerate(s):
            value = t_index_dict.get(v)
            if not value:
                return False
            check = False
            for index in value:
                if index > before_index:
                    before_index = index
                    check = True
                    break
            if not check:
                return False
        
        return True
