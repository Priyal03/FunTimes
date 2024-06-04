class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        def divideandconcur(nums, left, right):
            if left > right:
                return -math.inf

            mid = (left + right) // 2

            leftmax = rightmax = currsum = 0

            for i in range(mid - 1, left - 1, -1):
                currsum += nums[i]
                leftmax = max(leftmax, currsum)

            currsum = 0
            for i in range(mid + 1, right + 1):
                currsum += nums[i]
                rightmax = max(rightmax, currsum)

            currsum = rightmax + leftmax + nums[mid]

            leftsum = divideandconcur(nums, left, mid - 1)
            rightsum = divideandconcur(nums, mid + 1, right)

            return max(leftsum, rightsum, currsum)

        return divideandconcur(nums, 0, len(nums) - 1)
