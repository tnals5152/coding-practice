class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        num_str = str(num)
        
        for index in range(0, len(num_str) - k + 1):
            now_num = int(num_str[index : index + k])
            if now_num != 0 and num % now_num == 0:
                count += 1
                
        return count
