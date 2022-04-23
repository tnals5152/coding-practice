from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        que = deque()
        already_col = set()#이미 더한 것을 저장해준다.
        que.append((0, 0))#total_amount, add_count
        while que:
            total, count = que.popleft()
            
            if total == amount:
                return count
            if total > amount:
                continue
            
            remain = total - amount
            
            for i, v in enumerate(coins):
                #count가 점점 늘어나서 que에 넣어지므로 already_col에 있으면 count가 더 작은 것으로 들어가 있는 것
                if v >= remain and total + v not in already_col:
                    que.append((total + v, count + 1))
                    already_col.add(total + v)
        
        return -1
        
