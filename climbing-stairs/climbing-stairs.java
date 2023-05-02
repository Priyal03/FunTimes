class Solution {
    public int climbStairs(int n) {
        int memo[]=new int[n+1];
        return climb(n,0,memo);
    }

    private int climb(int n, int i, int[] memo){
        if(i>n)
            return 0;
        if(memo[i]>0){
            return memo[i];
        }
        if(n==i)
            return 1;//adding one for one path found.

        memo[i]=climb(n,i+1,memo)+climb(n,i+2,memo);
        return memo[i];
    }
}