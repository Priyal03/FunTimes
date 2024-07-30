class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = 0
        rightmax = 0
        ans = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            if height[left] < height[right]:
                leftmax = max(leftmax, height[left])
                ans += leftmax - height[left]
                left += 1
            else:
                rightmax = max(rightmax, height[right])
                ans += rightmax - height[right]
                right -= 1

        return ans
