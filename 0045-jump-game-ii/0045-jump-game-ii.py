class Solution:
    def jump(self, nums: List[int]) -> int:
        endPointer=0
        farthestReach=0
        steps=0

        for i in range(len(nums)-1):
            
            farthestReach=max(farthestReach,nums[i]+i)

            if i==endPointer:
                endPointer=farthestReach
                steps+=1

        return steps
