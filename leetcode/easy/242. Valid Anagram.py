from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = sorted([(key, value) for key, value in Counter(list(s)).items()])
        t_dict = sorted([(key, value) for key, value in Counter(list(t)).items()])

        if s_dict == t_dict:
            return True
        
        return False
