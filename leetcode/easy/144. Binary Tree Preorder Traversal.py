# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.call_next_node(root)
    
    def call_next_node(self, node: Optional[TreeNode]):
        if not node:
            return []
        return [node.val] + self.call_next_node(node.left) + self.call_next_node(node.right)
        
