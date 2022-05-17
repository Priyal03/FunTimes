class Solution {
    public void nextPermutation(int[] nums) {
        
        //returning for base case
        int n=nums.length-2;
        if(nums == null || n < 0 )
            return;
        
        //find index-1 which has lower value than current index
        while(n>=0 && nums[n] >= nums[n+1]){
            n--;
        }
        
        //if there still exist elements; then we gotta find biggeest element from last index to current index and swap them 
        if(n>=0){
            int index = nums.length - 1;
            
            while(nums[index] <= nums[n]){
                index--;
            }
            swap(nums,n,index);
        }
        
        //finally to get the next permute order, we have to reverse the remaining trail.
        reverse(nums,n+1, nums.length-1);
    }
    
    public void swap(int nums[], int x, int y){
        int temp=nums[x];
        nums[x]=nums[y];
        nums[y]=temp;
    }
    
    public void reverse(int[] nums, int index, int n){
        
        while(index<n){
            swap(nums,index,n);
            index++;
            n--;
        }
    }
}