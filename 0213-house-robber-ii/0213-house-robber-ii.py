class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def calc(start, end):
            lastHouse=nums[start]
            secondLastHouse = 0
        
            for i in range(start+1,end):
            
                temp = lastHouse
                lastHouse = max(secondLastHouse+nums[i] , lastHouse)
                secondLastHouse = temp

            return lastHouse

        n = len(nums)
        if n==1:
            return nums[0]
        return max(calc(0,n-1),calc(1,n))