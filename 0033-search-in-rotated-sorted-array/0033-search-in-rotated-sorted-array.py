class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        high=n-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                return mid
#left subarray of mid pointer is sorted
            elif nums[mid]>=nums[low]:
                if target>=nums[low] and target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
#right subaray of mid pointer is sorted.                
            else:
                if target<=nums[high] and target> nums[mid]:
                    low=mid+1
                else:
                    high=mid-1

        return -1