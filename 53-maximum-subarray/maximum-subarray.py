class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        windowsum = nums[0]

        for right in range(1, len(nums)):
            windowsum += nums[right]
            windowsum = max(
                windowsum, nums[right]
            )  # take current element if sum becomes lesser than that.
            maxsum = max(maxsum, windowsum)

        return maxsum
