# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        length -= n

        prehead = ListNode(-1)
        prehead.next = head
        first = prehead
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next

        return prehead.next
