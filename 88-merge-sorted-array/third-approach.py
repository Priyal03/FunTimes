class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1=m-1
        p2=n-1
#two pointers p1 and p2  to copy both arrays 
#use p for n+m range in resultant array nums1
        for p in range(n+m-1, -1, -1):
            if p2 < 0 : 
                #break out when nums2 is completely traversed.
                break
            if p1>=0 and nums1[p1] > nums2[p2]:
                #whenever nums1 is greater than nums2 is the right value when traversing from end.
                nums1[p] = nums1[p1]
                p1 -=1
            else:
                nums1[p]=nums2[p2]
                p2 -= 1
                
        
