//package ctp;

import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		
		PriorityQueue<Integer> pqMax=new PriorityQueue<>(Collections.reverseOrder());
		PriorityQueue<Integer> pqMin=new PriorityQueue<>();
		
		int n=Integer.parseInt(br.readLine());
		for(int i = 0;i<n;i++) {
			int num=Integer.parseInt(br.readLine());
			if(pqMax.size()<=pqMin.size()){
				pqMax.offer(num);
			}
			else {
				pqMin.offer(num);
			}
			
			// 그리고 비교해서 바꿔야 하면 바꾸기
			if(!pqMin.isEmpty()&& pqMax.peek()>pqMin.peek()) {
				int maxNum=pqMax.poll();
				int minNum=pqMin.poll();
				pqMax.offer(minNum);
				pqMin.offer(maxNum);
			}
			bw.write(pqMax.peek()+"\n");
			
		}
		
		br.close();
		bw.flush();
		bw.close();
	}
	
	
}

