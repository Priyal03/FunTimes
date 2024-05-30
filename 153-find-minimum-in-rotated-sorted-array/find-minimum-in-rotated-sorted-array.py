class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        if high == 0:
            return nums[0]

        if nums[0] < nums[high]:
            return nums[0]

        while low < high:
            midIndex = low + (high - low) // 2
            if nums[midIndex] < nums[high]:
                high = midIndex
            else:
                low = midIndex + 1

        return nums[low]
