class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        asum = sum(nums)
        
        if asum % 2 != 0:
            return False

        allSum = set()
        allSum.add(0)
        half = asum // 2

        for x in nums:

            temp = set(allSum)
            
            for y in allSum:
                temp.add(x + y)
            allSum = temp

            if half in allSum:
                return True

        return False
