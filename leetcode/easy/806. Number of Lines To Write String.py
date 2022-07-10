class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        #ord(s) - 97
        now_line = 0#max 100
        line = 1
        
        for alphabet in s:
            index = ord(alphabet) - 97
            if now_line + widths[index] > 100:
                now_line = widths[index]
                line += 1
            else:
                now_line += widths[index]
        
        return [line, now_line]
        