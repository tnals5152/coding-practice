class Solution:
    def sortSentence(self, s: str) -> str:
        return " ".join([v[:-1] for v in sorted(s.split(" "), key= lambda x: int(x[-1]))])
        
