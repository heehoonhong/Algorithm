//package ctp;

import java.util.*;


public class Main {
	
	public Queue<Integer> solution(int n,int k) {
		Queue<Integer> answer=new LinkedList<>();
		Queue<Integer> queue=new LinkedList<>();
		for(int i = 0;i<n;i++) {
			queue.offer(i+1);
		}
		
		for(int i = 0;i<n;i++) {
			for(int j = 0;j<k-1;j++) {
				int num=queue.poll();
				queue.offer(num);
			}
			answer.offer(queue.poll());
		}
		
		
		return answer;
	}
	
	public static void main(String[] args) {
		Main T = new Main();
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int k=sc.nextInt();
		Queue<Integer> result=T.solution(n, k);
		List<String> resultList=new ArrayList<>();
		
		for(int element:result) {
			resultList.add(String.valueOf(element));
		}
		
		System.out.println("<"+String.join(", ", resultList)+">");
	
	}

}
