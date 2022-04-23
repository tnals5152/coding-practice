from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        que = deque()
        que.append((root, [], 0))#next_node, now_added_list, total
        
        while que:
            node, added_list, total = que.popleft()
            
            if not node:#노트의 val없으면 종료
                continue
            
                
            added_list.append(node.val)
            total += node.val
            
            if total == targetSum and not node.left and not node.right:
                result.append(added_list)
                continue

            que.append((node.left, added_list[::], total))
            que.append((node.right, added_list[::], total))
            
            
        
        return result
            
        
