class Solution:
    def canJump(self, nums: List[int]) -> bool:

        lastIndex = len(nums) - 1

        for i in range(lastIndex - 1, -1, -1):
            jump = nums[i]
            pos = i
            if pos + jump >= lastIndex:
                lastIndex = pos

        return lastIndex == 0
