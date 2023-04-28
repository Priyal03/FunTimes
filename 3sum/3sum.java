class Solution {
    public List < List < Integer >> threeSum(int[] nums) {

        List < List < Integer >> ans = new ArrayList < > ();

        Arrays.sort(nums);

        int  n = nums.length;

        for (int i = 0; i < n && nums[i] <= 0; ++i) {
            
            Set<Integer> tracker = new HashSet<Integer>();//

            if (i > 0 && nums[i - 1] == nums[i]) {
                continue;
            }
                    
            for(int j=i+1; j<n; ++j){
                    
                    int complement = -nums[i]-nums[j];
                    
                    if(tracker.contains(complement)){
                        
                        ans.add(Arrays.asList(nums[i],nums[j],complement));
                        
                        while(j<n-1 && nums[j]==nums[j+1])
                            ++j;//move forward when dups
                        
                    }else{
                         tracker.add(nums[j]);//add to the hashset to compare the complement later
                    }    
                }
            }
        
        return ans;
    }
}