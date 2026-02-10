import java.util.*;
import java.io.*;


class Solution {
    public static class Node{
        int num;
        int index;
        public Node(int num,int index){
            this.num=num;
            this.index=index;
        }
        
    }
    
    public int[] solution(String[] operations) {
        PriorityQueue<Node> pq1=new PriorityQueue<>((o1,o2)->Integer.compare(o1.num,o2.num));
        PriorityQueue<Node> pq2=new PriorityQueue<>((o1,o2)->Integer.compare(o2.num,o1.num));
        int[] deleted=new int[operations.length];
        
        for(int i = 0;i<operations.length;i++){
            StringTokenizer st=new StringTokenizer(operations[i]);
            String command=st.nextToken();
            int num=Integer.parseInt(st.nextToken());
            if(command.equals("I")){
                pq1.offer(new Node(num,i));
                pq2.offer(new Node(num,i));
                deleted[i]=1;
            }
            else{
                if(num==1){
                    // 최댓값 삭제
                    while(!pq1.isEmpty() && deleted[pq1.peek().index]!=1){
                        pq1.poll();
                    }
                    while(!pq2.isEmpty()&&deleted[pq2.peek().index]!=1){
                        pq2.poll();
                    }
                    if(!pq2.isEmpty()){
                        deleted[pq2.peek().index]=0;
                        pq2.poll();
                    }
                }
                else{
                    // 최솟값 삭제
                    while(!pq1.isEmpty() && deleted[pq1.peek().index]!=1){
                        pq1.poll();
                    }
                    while(!pq2.isEmpty()&&deleted[pq2.peek().index]!=1){
                        pq2.poll();
                    }
                    if(!pq1.isEmpty()){
                        deleted[pq1.peek().index]=0;
                        pq1.poll();
                    }
                    
                }
                
                
            }
        }
        int[] answer=new int[2];
        while(!pq1.isEmpty() && deleted[pq1.peek().index]!=1){
            System.out.println(pq1.peek().num);
            pq1.poll();
        }
        while(!pq2.isEmpty()&&deleted[pq2.peek().index]!=1){
            System.out.println(pq2.peek().num);
            pq2.poll();
        }
        if(!pq2.isEmpty()){
            
        }
        if(!pq1.isEmpty()){
            
        }
        
        if(!pq1.isEmpty()){
            answer[1]=pq1.peek().num;
        }
        if(!pq2.isEmpty()){
            answer[0]=pq2.peek().num;
        }
        return answer;
        
    }
}