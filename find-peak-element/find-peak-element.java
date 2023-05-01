class Solution {
    
    public int findPeakElement(int[] nums) {
    int n = nums.length;
        
    for (int i = 0; i < n; i++) {
        boolean isPeak = true;
        if (i > 0 && nums[i] <= nums[i - 1]) {
            isPeak = false;
        }
        if (i < n - 1 && nums[i] <= nums[i + 1]) {
            isPeak = false;
        }
        if (isPeak) {
            return i;
        }
    }
    return -1;
}

}