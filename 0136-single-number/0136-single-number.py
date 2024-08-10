class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniquelist = set()
        for x in nums:
            if x in uniquelist:
                uniquelist.remove(x)
            else:
                uniquelist.add(x)

        return uniquelist.pop()