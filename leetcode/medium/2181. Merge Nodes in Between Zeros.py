# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result_node = ListNode()
        node_copy = result_node
        total = 0
        
        while head:
            if head.val == 0:
                if total == 0:
                    pass
                else:
                    result_node.next = ListNode(val=total)
                    result_node = result_node.next
                    total = 0

            else:
                total += head.val
            head = head.next
        
        return node_copy.next
                    
        
        
        
        
        # 첫번째 방법
        result = []
        que = deque()
        que.append((0, head))
        
        while que:
            total, node = que.popleft()
            
            if node is None:
                if total != 0:
                    result.append(total)
                break
            
            if node.val == 0 and total != 0:
                result.append(total)
                total = 0
            
            que.append((total + node.val, node.next))
        
        return self.append_node(result)
    
    def append_node(self, val_list):
        if len(val_list) == 0:
            return None
        
        node = ListNode(val_list[0])
        node_copy = node
        
        for index, val in enumerate(val_list[:-1]):
            node.next = ListNode(val=val_list[index + 1])
            node = node.next

        return node_copy
