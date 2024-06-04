class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastIndex = len(nums) - 1
        for i in range(lastIndex - 1, -1, -1):

            if lastIndex - nums[i] - i <= 0:
                lastIndex = i

        return lastIndex == 0
