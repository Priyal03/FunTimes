# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        
        sum = 0
        dummy = ListNode(0)
        curr = dummy

        while l1 or l2 or sum!=0:
            first = l1.val if l1 else 0
            two = l2.val if l2 else 0
            sum += first + two

            node = ListNode(sum % 10) #ekam no ank joie answer ma
            curr.next = node
            curr = node

            sum = sum // 10 #dashak no ank joie remainder ma
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
