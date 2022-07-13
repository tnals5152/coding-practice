class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_index_dict = dict()
        s_list = s.split()
        
        if len(pattern) != len(s_list):
            return False
        
        for index, alphabet in enumerate(pattern):
            if word_index_dict.get(alphabet) is None:
                word_index_dict[alphabet] = set()
            word_index_dict[alphabet].add(s_list[index])
        
        value_set = set()

        for key, value in word_index_dict.items():
            if len(value) != 1:
                return False
            
            value_set.add(list(value)[0])
            
        if len(value_set) != len(word_index_dict.keys()):
            return False

        return True
