# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        now_node = head
        while now_node:
            if now_node.next and now_node.val == now_node.next.val:
                now_node.next = now_node.next.next
            else:
                now_node = now_node.next
        
        return head
