from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        r = re.compile("[a-z|A-Z]+")
        paragraph_list = r.findall(paragraph.lower())        
        word_list = sorted([(key, value) for key, value in Counter(paragraph_list).items()], key=lambda x:(-x[1]))
        banned_dict = dict()
        
        for ban in banned:
            banned_dict[ban] = True

        for (key, value) in word_list:
            if not banned_dict.get(key):
                return key
        return ""