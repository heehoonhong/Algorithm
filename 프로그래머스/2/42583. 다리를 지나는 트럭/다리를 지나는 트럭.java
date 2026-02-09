import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Deque<Integer> bridge=new ArrayDeque<>();
        for(int i = 0;i<bridge_length;i++){
            bridge.addLast(0);
        }
        Deque<Integer> trucks=new ArrayDeque<>();
        for(int i = 0;i<truck_weights.length;i++){
            trucks.addLast(truck_weights[i]);
        }
        int curWeight=0;
        int cnt=0;
        while(!trucks.isEmpty() || curWeight!=0){
            // 1. bridge에서 popleft
            // popleft한 만큼 curWeight에서 빼기(0인지 아닌지 구분)
            // curWeight+trucks.peekFirst()가 weight를 안넘는지 비교 후
            // 안 넘으면 bridge에 append하기 
            int curTruck=bridge.pollFirst();
            if(curTruck>0){
                curWeight-=curTruck;
            }
            if(!trucks.isEmpty() && curWeight+trucks.peekFirst()<=weight){
                int truck=trucks.pollFirst();
                curWeight+=truck;
                bridge.offerLast(truck);
                
            }
            else{
                bridge.offerLast(0);
            }
            cnt+=1;
            
        }
        return cnt;
    }
}