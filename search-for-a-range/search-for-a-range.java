class Solution {
    public int[] searchRange(int[] nums, int target) {
        
        int first = findBound(nums,target, true);
        
        if(first==-1){
            return new int[]{-1,-1};
        }
        
        int last = findBound(nums,target, false);
        return new int[]{first,last};
    }
    private int findBound(int arr[], int target, boolean isFirst){
        int n=arr.length,begin=0,end=n-1;
        while(begin<=end){
            int mid = (begin+end)/2;
            if(arr[mid]==target){
                if(isFirst){
                    if(mid==begin || arr[mid-1]!=target){
                        return mid;
                    }
                    end = mid-1;
                }else{
                    if(mid==end || arr[mid+1]!=target){
                        return mid;
                    }
                    begin=mid+1;
                }
            }else if(arr[mid]>target){
                end=mid-1;
            }else{
                begin=mid+1;
            }
        }
        return -1;
    }
}