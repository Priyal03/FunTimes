class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minproduct, maxproduct = 1,1
        res = max(nums)

        for x in nums:

            temp = maxproduct*x
            maxproduct = max(temp, minproduct*x, x)
            minproduct = min(temp, minproduct*x, x)
            
            res = max(maxproduct, res)

        return res