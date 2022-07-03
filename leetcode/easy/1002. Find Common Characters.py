from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter_dict = dict()
        result = []
        
        for word in words:
            word_dict = Counter(word)
            
            for key in word_dict.keys():
                if counter_dict.get(key) is None:
                    counter_dict[key] = []
                    
                counter_dict[key].append(word_dict[key])
        
        
        for key in counter_dict.keys():
            if len(counter_dict[key]) == len(words):
                result.extend([key] * min(counter_dict[key]))
        
        return result
