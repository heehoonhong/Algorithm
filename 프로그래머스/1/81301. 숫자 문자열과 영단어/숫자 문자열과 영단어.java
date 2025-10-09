class Solution {
    public int solution(String s) {
        String[] numArr={"zero","one","two","three","four","five","six","seven","eight","nine","ten"};
        
        for(int i=0;i<numArr.length;i++){   
            s=s.replaceAll(numArr[i],String.valueOf(i));
        }
        
        return Integer.parseInt(s);
    }
}