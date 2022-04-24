# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        que = deque()
        que.append((root, False))#left일 시 True, else False
        
        while que:
            node, left = que.popleft()
            
            if not node:
                continue
            if left and not node.left and not node.right:
                total += node.val

            que.append((node.left, True))
            que.append((node.right, False))
        
        return total
