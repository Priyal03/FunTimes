class Solution:
    def findMin(self, array: List[int]) -> int:
        left=0
        right = len(array)-1

        if array[right]>array[0] or right==0:
            return array[0]

        while left<right:
            mid = (left+right)//2

            if array[mid]>array[mid+1]:
                return array[mid+1]

            if array[mid-1]>array[mid]:
                return array[mid]

            if array[mid]>array[0]:
                left=mid+1
            else:
                right=mid-1

