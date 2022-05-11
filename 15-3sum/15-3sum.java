class Solution {
    public List < List < Integer >> threeSum(int[] nums) {
//chotu
        List < List < Integer >> ans = new ArrayList < > ();
        if (nums.length < 3)
            return ans;

        Arrays.sort(nums);

        int left = 0, n = nums.length, right = n - 1;

        for (int i = 0; i < n && nums[i] <= 0; ++i) {

            if (i == 0 || nums[i - 1] != nums[i]) {
                
                Set<Integer> store = new HashSet<Integer>();//storage for complement 
                
                for(int j=i+1; j<n; j++){
                    
                    int complement = -nums[i]-nums[j];
                    
                    if(store.contains(complement)){
                        
                        ans.add(Arrays.asList(nums[i],nums[j],complement));
                        
                        while(j+1 < n && nums[j]==nums[j+1])
                            ++j;
                        
                    }
                    store.add(nums[j]);
                }
            }
        }
        return ans;
    }
}