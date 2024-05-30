# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        starthead = ListNode(-1)
        mergelist = starthead
        while list1 and list2:
            #keep adding smaller value and iterating to next node
            if list1.val<list2.val:
                mergelist.next = list1
                list1=list1.next
            else:
                mergelist.next=list2
                list2=list2.next

            mergelist=mergelist.next

#add remaining elements after compare
        mergelist.next = list1 if list1 is not None else list2

        return starthead.next
        