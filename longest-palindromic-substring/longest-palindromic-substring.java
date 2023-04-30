class Solution {
    public String longestPalindrome(String s) {
    
    int n=s.length(), maxLength=1, start=0;
    boolean dp[][]=new boolean[n][n];
    for(int i=0;i<n;i++){
        dp[i][i]=true;//base case
    }

    for(int len = 2; len<=n ; len++){//length runs from 1 to n
        for(int i=0;i<=n-len;i++){ //check for all indexes
            int j = i+len-1;
            if(s.charAt(j)==s.charAt(i)){
                if(dp[i+1][j-1] || len==2){ //len 2 need to be marked as true to give it a chance to fail or succeed further.
                    dp[i][j]=true;
                    if(len>maxLength){
                        maxLength=len;
                        start=i;
                    }
                }
            }
        }
    }
    return s.substring(start,start+maxLength);
}
}