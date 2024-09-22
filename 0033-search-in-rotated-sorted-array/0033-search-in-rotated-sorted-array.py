class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        high=n-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]>nums[-1]:
                low=mid+1
            else:
                high=mid-1
            
        inflectionPoint = low
        degreeOfRotataion = n - inflectionPoint

        low = (degreeOfRotataion + inflectionPoint) % n
        high = (degreeOfRotataion + inflectionPoint - 1) % n

        while low<=high:
            
            mid=low+(high-low)//2
            newMid = (mid - degreeOfRotataion)%n

            if nums[newMid]==target:
                return newMid
            elif nums[newMid]>target:
                high=mid-1
            else:
                low=mid+1

        return -1