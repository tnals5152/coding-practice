class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count_check = dict()
        result = []
        
        for s in s1.split() + s2.split():
            count_check.setdefault(s, 0)
            count_check[s] += 1
        
        for key in [key for key, value in count_check.items() if value == 1]:
            result.append(key)
            
        return result

        
