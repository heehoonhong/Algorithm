import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> queue=new LinkedList<>();
        Queue<Integer> bridgeQueue=new LinkedList<>();
        
        for(int i = 0;i<truck_weights.length;i++){
            queue.offer(truck_weights[i]);
        }
        
        for(int i = 0;i<bridge_length;i++){
            bridgeQueue.offer(0);
        }
        
        int time=0;
        int currentWeight=0;
        while(!queue.isEmpty()){
            time++;
            
            currentWeight-=bridgeQueue.poll();
            
            if(currentWeight+queue.peek()<=weight){
                int truckToLoad=queue.poll();
                bridgeQueue.offer(truckToLoad);
                currentWeight+=truckToLoad;
            }
            else{
                bridgeQueue.offer(0);
            }
            
        }
        
        return time+bridgeQueue.size();
    }
}