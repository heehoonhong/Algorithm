class Solution {
    public int[] solution(String s) {
        int[] answer = {0,0};
        
        while(!s.equals("1")){
            String temp="";
            for(int i=0;i<s.length();i++){
                if(s.charAt(i)=='1'){
                    temp+="1";
                }
                else{
                    answer[1]++;
                }
            }
            s=temp;
            
            s=Integer.toBinaryString(s.length());
            answer[0]++;
        }
        
        
        return answer;
    }
}