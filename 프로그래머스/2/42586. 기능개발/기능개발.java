import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Stack<Integer> stack=new Stack<>();
        List<Integer> answer=new ArrayList<>();
        for(int i=progresses.length-1;i>=0;i--){
            stack.push((int)Math.ceil((100.0-progresses[i])/speeds[i]));
        }
        
        while(!stack.isEmpty()){
            int checkDay=stack.pop();
            int count=1;
            
            while(!stack.isEmpty()&&stack.peek()<=checkDay){
                stack.pop();
                count++;
            }
            answer.add(count);
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}