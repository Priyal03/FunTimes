# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        head=ListNode(0)
        curr = head

        while l1 or l2 or carry!=0:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            columnSum = first+second+carry

            newNode = ListNode(columnSum%10) #unit digit for answer
            curr.next = newNode
            curr = curr.next
 
            carry = columnSum//10 #this is for carry forward to next iteration (vaddi)
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return head.next