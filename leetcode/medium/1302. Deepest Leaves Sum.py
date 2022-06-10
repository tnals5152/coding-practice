# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        result = []
        max_depth = 0
        que = deque()
        que.append((0, root))
        
        while que:
            depth, node = que.popleft()
            
            if node is None:
                continue
            
            if node.left is None and node.right is None:
                result.append([depth, node.val])
                max_depth = max(max_depth, depth)
                continue
            
            que.append((depth + 1, node.left))
            que.append((depth + 1, node.right))
        
        
        
        return sum([v[1] for v in result if v[0] == max_depth])
            
