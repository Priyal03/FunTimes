class Solution:
    def maxArea(self, height: List[int]) -> int:

        startLine =0
        endLine = len(height)-1
        maxarea = 0
        while startLine<endLine:
            area = min(height[startLine],height[endLine])*abs(endLine-startLine)
            maxarea = max(area,maxarea)
            if height[startLine]>height[endLine]:
                endLine -=1
            else:
                startLine+=1
        return maxarea