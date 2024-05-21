class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minindex = nums.index(min(nums))
        # maxval = max(nums)
        # maxindex = nums[::-1].index(maxval)
        n = len(nums)-1
        maxval = 0
        maxindex = 0
        for i,v in enumerate(nums):
            if v >= maxval:
                maxval = v
                maxindex = i

        count = minindex + (n-maxindex)

        if minindex > maxindex:
            return count-1 #one less swap for this condition

        return count