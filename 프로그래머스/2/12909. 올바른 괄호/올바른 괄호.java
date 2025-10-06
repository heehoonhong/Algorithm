import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack=new Stack<>();
        char[] c=s.toCharArray();
        
        for(int i=0;i<c.length;i++){
            if(c[i]=='('){
                stack.push(c[i]);
            }
            else{
                if(!stack.isEmpty()){
                    stack.pop();
                }
                else{
                    return false;
                }
            }
        }
        
        if(stack.isEmpty()){
            return true;
        }
        else{
            return false;
        }
    }
}