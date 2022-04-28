# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_list = []
        
        while head:
            head_list.append(head.val)
            head = head.next
        
        head_list.sort(reverse=True)
        
        head2 = None
        
        for v in head_list:
            node = ListNode(v, head2)
            head2 = node
            
        return head2
