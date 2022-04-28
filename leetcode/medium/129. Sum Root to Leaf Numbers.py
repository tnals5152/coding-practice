# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        que = deque()
        if not root:
            return 0
        
        que.append((root, 0))#node, total
        
        while que:
            node, now_sum = que.popleft()
            
            now_sum = now_sum * 10 + node.val
            
            if not node.left and not node.right:
                total += now_sum
                continue

            for now_node in [node.left, node.right]:
                if now_node:
                    que.append((now_node, now_sum))
        
        return total
