class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i1, i2 = 0, 0
        result = False
        
        while i1 < len(name) and i2 < len(typed):
            
            if name[i1] == typed[i2]:
                i1 += 1
                i2 += 1
            else:
                if i1 != 0 and name[i1 - 1] == typed[i2]:
                    i2 += 1
                else:
                    return False
                
        if i1 >= len(name) and (i2 >= len(typed) or "".join(list(set(typed[i2:]))) == name[-1]):
            return True
        return False
