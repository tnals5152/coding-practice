# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        que = deque()
        que.append(root)
        result_sum = 0
        
        while que:
            node = que.popleft()
            if node == None:
                continue
            
            if node.val >= low and node.val <= high:
                result_sum += node.val
                
            que.append(node.left)
            que.append(node.right)
        
        return result_sum
