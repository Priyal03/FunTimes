class Solution {
    public boolean winnerOfGame(String colors) {

            if(colors.length()<3)
                return false;
        int countA=0, countB=0;
        for (int i = 1; i < colors.length()-1 ; i++) {

            if(colors.charAt(i)=='A' && colors.charAt(i-1)=='A' && colors.charAt(i+1)=='A'){
                countA++;
            }
            if(colors.charAt(i)=='B' && colors.charAt(i-1)=='B' && colors.charAt(i+1)=='B'){

                countB++;}
        }
        return (countA-countB)>0?true:false;
    }
}