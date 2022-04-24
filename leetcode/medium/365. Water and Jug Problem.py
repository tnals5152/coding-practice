from collections import deque
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        min_capacity, max_capacity = min(jug1Capacity, jug2Capacity), max(jug1Capacity, jug2Capacity)
        if min_capacity + max_capacity == targetCapacity:
            return True
        que = deque()
        already_col = set()#이미 계산한 값 넣기
        que.append((0, max_capacity))#jug1 amount now, jug2 amount now
        
        while que:
            jug1, jug2 = que.popleft()
            
            remain = (jug1 + jug2) % min_capacity
            jug1, jug2 = remain, max_capacity
            

            if targetCapacity in [jug1, jug2, jug1 + jug2, jug1 + min_capacity]:
                return True
            
            if jug1 not in already_col:
                already_col.add(jug1)
                que.append((jug1, jug2))
        
        return False
                
            
