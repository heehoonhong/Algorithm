import java.util.*;

class Solution {
    
    public static class Process{
        int priority;
        int position;
    
        public Process(int priority,int position){
            this.priority=priority;
            this.position=position;
        }
    }
    
    public int solution(int[] priorities, int location) {
        Queue<Process> queue=new LinkedList<>();
        PriorityQueue<Integer> remainPriority=new PriorityQueue<>(Collections.reverseOrder());
        
        // 프로세스 큐 추가
        for(int i =0;i<priorities.length;i++){
            queue.add(new Process(priorities[i],i));
            remainPriority.add(priorities[i]);
        }
        
        int order=1;
        while(true){
            Process ready=queue.poll();
            int maxPriority=remainPriority.poll();
            if(maxPriority==ready.priority){
                if(location==ready.position){
                    return order;
                }
                else{
                    order++;
                }
            }
            else{
                queue.add(ready);
                remainPriority.add(maxPriority);
            }
        }
        
        
    }
}