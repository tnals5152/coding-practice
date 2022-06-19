from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        root_dict = dict()
        last_num = len(graph) - 1
        que = deque()
        result = []
        
        for index, num_list in enumerate(graph):
            for num in num_list:
                if root_dict.get(num) is None:
                    root_dict[num] = []
                root_dict[num].append(index)
        
        que.append((last_num, [last_num]))
        
        while que:
            now_num, visited = que.popleft()
            
            if now_num == 0:
                result.append(visited)
                continue
            
            if root_dict.get(now_num):
                for num in root_dict[now_num]:
                    que.append((num, [num] + visited))
            
            
        
        return result