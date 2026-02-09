import java.util.*;

class Solution {
    boolean solution(String s) {
        char[] ss=s.toCharArray();
        Queue<Character> queue=new LinkedList<>();
        for(int i = 0;i<ss.length;i++){
            if(ss[i]=='('){
                queue.offer(ss[i]);
            }
            else{
                if(!queue.isEmpty()){
                    queue.poll();
                }
                else{
                    return false;
                }
            }
        }
        if(!queue.isEmpty()){
            return false;
        }
        else{
            return true;
        }
    }
    
}