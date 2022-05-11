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
                left = i + 1;
                right = n - 1;

                while (left < right) {
                    int sum = nums[left] + nums[right] + nums[i];
                    if (sum == 0) {

                        List < Integer > list = new ArrayList < Integer > ();
                        list.add(nums[left++]);
                        list.add(nums[i]);
                        list.add(nums[right--]);

                        ans.add(list);

                        //when we have duplicates**
                        while (left < right && nums[left] == nums[left - 1])
                            ++left;

                    } else if (sum < 0) {

                        ++left;
                    } else {

                        --right;
                    }
                }
            }
        }
        return ans;
    }
}