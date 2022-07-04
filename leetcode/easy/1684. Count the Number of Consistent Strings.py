class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        
        for word in words:
            check = True
            for s in word:
                if s not in allowed:
                    check = False
                    break
            
            if check:
                result += 1
        
        return result