import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> result=new LinkedList<>();
        Queue<Integer> queue=new LinkedList<>();
        for(int i = 0;i<progresses.length;i++){
            if((100-progresses[i])%speeds[i]==0){
                queue.offer((100-progresses[i])/speeds[i]);
            }
            else{
                queue.offer((100-progresses[i])/speeds[i]+1);
            }
        }
        
        while(!queue.isEmpty()){
            int cnt=0;
            int cur=queue.poll();
            cnt+=1;
            while((!queue.isEmpty()) && cur>=queue.peek()){
                queue.poll();
                cnt+=1;
            }
            result.offer(cnt);
        }
        int[] answer=new int[result.size()];
        for(int i = 0;i<answer.length;i++){
            answer[i]=result.poll();
        }
        return answer;
    }
}