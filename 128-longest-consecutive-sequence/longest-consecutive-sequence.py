class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxseq = 0
        nums.sort()
        current=1
        for i in range(1,len(nums)):
            
            if (nums[i]-1)==nums[i-1]:
                current+=1
            elif nums[i]==nums[i-1]:
                #do nothing because we are trying to find longest distinct characters.
                continue
            else:
                maxseq = max(maxseq,current)
                current=1

        return max(maxseq,current)