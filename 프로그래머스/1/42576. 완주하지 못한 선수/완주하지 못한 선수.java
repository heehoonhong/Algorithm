import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String,Integer> users= new HashMap<>();
        String answer="";
        for(String p:participant){
            users.put(p,users.getOrDefault(p,0)+1);
        }
        for(String c:completion){
            int value=users.get(c);
            value--;
            users.put(c,value);
        }
        for(String p:users.keySet()){
            if(users.get(p)==1){
                answer+=p;
            }
        }
        return answer;
    }
}