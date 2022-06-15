class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        before = 0
        
        for b in bank:
            now = b.count("1")
            if now == 0:
                continue
            result += before * now
            before = now
        
        return result
