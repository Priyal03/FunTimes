class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxseq = 0
        hset = set(nums)

        for val in nums:
            if val-1 not in hset:
                next = val+1
                current=1

                while next in hset:
                    next+=1
                    current+=1
                
                maxseq = max(maxseq,current)

        return maxseq