class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        currJump = maxJump = 0
        for i in range(n - 1):
            # keep updating the max jump you can make
            maxJump = max(maxJump, i + nums[i])
            # increase the counter only when your index reaches maxpossiblejump for current maxJump value, and now make that variable ready for next count by storing maxJump
            if i == currJump:
                count += 1
                currJump = maxJump
        return count
