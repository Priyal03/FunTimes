class Solution:
    def rob(self, nums: List[int]) -> int:

        twoStepLast = 0
        lastElement = nums[0]

        for i in range(1,len(nums)):

            temp = lastElement
            lastElement = max(nums[i] + twoStepLast, lastElement)
            twoStepLast = temp

        return lastElement
#slicing the substring every time is more costlier than using a range from 1 to n.