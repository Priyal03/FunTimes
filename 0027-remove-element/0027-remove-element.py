class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        notRare=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[notRare] = nums[i]
                notRare+=1
        
        return notRare
