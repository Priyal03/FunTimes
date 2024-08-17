class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=0
        
        for i in range(len(nums)):
            if nums[i]==0:
                nums[zero],nums[i]=nums[i],nums[zero]
                zero+=1
                
        for i in range(len(nums)):
            if nums[i]==1:
                nums[zero],nums[i]=nums[i],nums[zero]
                zero+=1