class Solution:
    def rob(self, nums: List[int]) -> int:

        twoStepLast = 0
        lastElement = nums[0]

        for curr in nums[1:]:

            temp = lastElement
            lastElement = max(curr + twoStepLast, lastElement)
            twoStepLast = temp

        return lastElement
