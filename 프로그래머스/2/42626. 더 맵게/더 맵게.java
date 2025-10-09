import java.util.*;

class Solution {
    
    public static Queue<Integer> queue;
    
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        queue=new PriorityQueue<>();
        for(int i=0;i<scoville.length;i++){
            // 데이터 삽입
            queue.offer(scoville[i]);
        }
        
        while(queue.peek()<K){
            
            if(queue.size()==1){
                answer=-1;
                break;
            }
            
            int first=queue.poll();
            int second=queue.poll();
            int newFood=first+2*second;
            queue.offer(newFood);
            answer++;
        }
        
        return answer;
    }
}