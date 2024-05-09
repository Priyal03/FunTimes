class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}
        for i in range(len(nums)):
            
            diff = target-nums[i]

            if diff in map:#search the difference in map's key
                return [i,map[diff]]#return the stored index
            
            map[nums[i]]=i 

            #storing index at the map's value.

        #return [0,0]