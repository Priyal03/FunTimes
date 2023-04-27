class Solution {
    public void sortColors(int[] nums) {
        //dual pivoting for quick sort algo

        //same logic as before but in quick sort fashion
    int lo = 0, hi = nums.length - 1, i = 0;
    
    while (i <= hi) {
        if      (nums[i] == 0) swap(nums, lo++, i++);
        else if (nums[i] == 2) swap(nums, i, hi--);
        else if (nums[i] == 1) i++;
    }
}

private void swap(int[] nums, int i, int j) {
    int t = nums[i];
    nums[i] = nums[j];
    nums[j] = t;
}
}