//package ctp;

import java.io.*;
import java.util.*;

public class Main {
	
	public static class Node{
		int s;
		int t;
		public Node(int s,int t) {
			this.s=s;
			this.t=t;
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		List<Node> classList=new ArrayList<>();
		PriorityQueue<Integer> pq=new PriorityQueue<>(); 
		int n=Integer.parseInt(br.readLine());
		for(int i = 0;i<n;i++) {
			StringTokenizer st=new StringTokenizer(br.readLine());
			int s=Integer.parseInt(st.nextToken());
			int t=Integer.parseInt(st.nextToken());
			classList.add(new Node(s,t));
		}
		classList.sort((o1,o2)->o1.s-o2.s);
		pq.offer(classList.get(0).t);
		for(int i=1;i<classList.size();i++) {
			int ss=classList.get(i).s;
			int tt=classList.get(i).t;
			if(pq.peek()<=ss) {
				pq.poll();
				pq.offer(tt);
			}
			else {
				pq.offer(tt);
			}
		}
		
		bw.write(pq.size()+"\n");
		br.close();
		bw.flush();
		bw.close();
	}
	
	
}

