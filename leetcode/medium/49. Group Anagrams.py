class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alpha_dict = dict()#{"aet": ["ate", "eat", "tea"]}
        result = []
        for s in strs:
            key = "".join(sorted(s))
            if alpha_dict.get(key):
                alpha_dict[key].append(s)
            else:
                alpha_dict[key] = [s]
        return [value for _, value in alpha_dict.items()]
        
