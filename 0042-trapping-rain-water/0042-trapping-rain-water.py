class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        ans = 0
        leftmax=0
        rightmax=0
        while left<right:
            if height[left]<height[right]:
                leftmax = max(leftmax,height[left])
                ans += leftmax-height[left]
                left+=1
            else:
                rightmax = max(rightmax,height[right])
                ans += rightmax - height[right]
                right-=1
        return ans