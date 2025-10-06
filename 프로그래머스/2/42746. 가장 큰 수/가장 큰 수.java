import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
    
        String[] str=new String[numbers.length];
        for(int i = 0;i<str.length;i++){
            str[i]=String.valueOf(numbers[i]);
        }
        
        Arrays.sort(str,(s1,s2)->(s2+s1).compareTo(s1+s2));
        
        for(String s:str){
            answer+=s;
        }
        
        if(answer.charAt(0) == '0'){
            answer = "0";
        }
        
        return answer;
    }
}