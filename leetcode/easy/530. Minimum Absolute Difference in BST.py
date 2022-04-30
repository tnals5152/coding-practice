# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = []
        que = deque()
        que.append(root)
        abs_result = 10 ** 5
        
        while que:
            
            node = que.popleft()
            
            if not node:
                continue
            
            result.append(node.val)
            que.append(node.left)
            que.append(node.right)
        
        result.sort()
        for i, v in enumerate(result[:-1]):
            abs_result = min(abs(v - result[i + 1]), abs_result)
            if abs_result == 0:
                return abs_result
            
        
        return abs_result
            
