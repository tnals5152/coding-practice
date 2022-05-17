from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = Counter(ransomNote)
        magazine_dict = Counter(magazine)

        for key, value in ransom_dict.items():
            if not magazine_dict.get(key):
                return False
            if value > magazine_dict[key]:
                return False
        return True
