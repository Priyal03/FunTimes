# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        prev = None
      
        while curr:
            nextNode = curr.next #save next element
            curr.next = prev #point the next pointer to previous element

            prev = curr #and just move the pointers to next after the operation
            curr = nextNode

        return prev
