class Solution {
    
    public int uniquePaths(int m, int n) {
        
        int dp[][]=new int[m+1][n+1];
        
        for(int[] array:dp){
            Arrays.fill(array,1);
        }
        
        for(int row = 1;row<m;++row){
            for(int col=1;col<n;++col){
                dp[row][col] = dp[row-1][col]+dp[row][col-1];      
            }
        }
        return dp[m-1][n-1];
}
}