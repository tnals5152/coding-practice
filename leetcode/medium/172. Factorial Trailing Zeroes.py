from collections import deque
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0: return 0
        que = deque()
        que.append((n, n - 1))
        
        while que:
            total, now_num = que.popleft()
            if now_num <= 1:
                count = 0
                for i in str(total)[::-1]:
                    if i != '0':
                        return count
                    count += 1
                return count
            total *= now_num
            que.append((total, now_num - 1))
        
