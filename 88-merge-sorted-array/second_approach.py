class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #take temp array to traverse from 0 to m elements of num1 list. 
        temparr = nums1[:m] #this is additional storage of O(m) >>> space complexity

        p1=0 #to traverse the temp array
        p2=0 #to traverse the nums2 array

#taking p just to go over whole resultant array
        for p in range(n+m):  # time complexity 2 times O(n+m)
            #p1 needs to be less than m to copy into resultant array and value needs to be lesser than second array
            if p2 >= n or (p1<m and temparr[p1] <= nums2[p2]):
                nums1[p]=temparr[p1]
                p1 +=1
            else:#p2 needs to be less than n to copy nums2 into resultant array
                nums1[p]=nums2[p2]
                p2+=1
