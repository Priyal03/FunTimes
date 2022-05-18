class Solution {
    public String multiply(String num1, String num2) {
        
        StringBuilder sb1 = new StringBuilder(num1);
        StringBuilder sb2 = new StringBuilder(num2);
        
        if (num1.equals("0") || num2.equals("0")) {
            return "0";
        }
        
        
        int n = sb1.length() + sb2.length();
        
        sb1.reverse();
        sb2.reverse();
        
        StringBuilder answer = new StringBuilder();
        for(int i=0;i<n;i++){
            answer.append(0);
        }
        
        for(int i=0;i<sb2.length();i++){
            int digit2 = sb2.charAt(i)-'0';
            
            for(int j=0;j<sb1.length();j++){
                
                int digit1=sb1.charAt(j)-'0';
                int currentIndex = i+j;
                
                int carry = answer.charAt(currentIndex)-'0';
                int mul = digit1*digit2+carry;
                
                answer.setCharAt(currentIndex, (char)(mul % 10 + '0'));
                int value = (answer.charAt(currentIndex + 1) - '0') + mul / 10;
                answer.setCharAt(currentIndex + 1, (char)(value + '0'));
            
            }
        }
        
        if (answer.charAt(answer.length() - 1) == '0') {
            answer.deleteCharAt(answer.length() - 1);
        }
        
        answer.reverse();
        return answer.toString();
    }
        
}