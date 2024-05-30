# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        nDistancePointer = head
        first = dummy ##if you do not use dummy, you will end up one node short of nth distance. 

        for _ in range(n):
            nDistancePointer = nDistancePointer.next

        while nDistancePointer:
            first = first.next
            nDistancePointer = nDistancePointer.next

        first.next = first.next.next

        return dummy.next
