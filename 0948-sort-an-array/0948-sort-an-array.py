class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
#follow divide and concur approach.. so in this function keep dividing in halves then in concur function perform comparision and merge into one array
        mid = len(nums)//2
        left_half = nums[:mid]
        right_half = nums[mid:]

        left_sorted = self.sortArray(left_half)
        right_sorted = self.sortArray(right_half)

        return self.concur(left_sorted, right_sorted)

    def concur(self, left, right):
        i=0
        j=0
        ans=[]
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                ans.append(left[i])
                i+=1
            else:
                ans.append(right[j])
                j+=1

        ans.extend(left[i:])
        ans.extend(right[j:])

        return ans
