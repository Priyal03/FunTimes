# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head

        curr = head
        next = head.next
        prev = self.reverseList(next)
        
        next.next = curr
        curr.next = None

        return prev