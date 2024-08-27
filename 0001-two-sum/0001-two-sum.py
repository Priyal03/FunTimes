class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed = {}

        for i,x in enumerate(nums):
            diff = target-x
            if diff in hashed:
                return [hashed[diff],i]
            hashed[x]=i

