class Solution {
    //time - O(n)
    //space - O(1)
    public int maxArea(int[] height) {
        
        int left = 0, n=height.length, right = n-1,area=0;
        
        while(left<right){
            
            area = Math.max(area,(right-left)*Math.min(height[left],height[right]));
            
            if(height[left]<=height[right])
                left++;//we have to move the lower side, because by moving one bar, we also decrease the width which is not favorable if we move the higher bar at a moment
            else
                right--;
        }
        
        return area;
    }
    //brute force is O(n2) for all the area comparisions
}