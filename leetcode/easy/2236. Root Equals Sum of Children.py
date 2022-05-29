# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return self.check_sum(root)
        
        
    def check_sum(self, node):
        if node == None or (node.left == None and node.right == None):
            return True
        if (node.left == None and node.right != None) or\
           (node.left != None and node.right == None):
            return False

        if node.val != node.left.val + node.right.val:
            return False
        
        return self.check_sum(node.left) and self.check_sum(node.right)
