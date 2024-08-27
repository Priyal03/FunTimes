class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset=set(nums)
        maxlen=0
        for left in nums:
            if left-1 not in hset:
                right=left
                while right in hset:
                    right+=1
                maxlen = max(maxlen, right-left)
        return maxlen