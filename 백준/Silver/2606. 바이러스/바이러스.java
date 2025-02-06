//package ctp;

import java.util.*;

public class Main {
	
	static ArrayList<ArrayList<Integer>> graph;
	static int[] ch,dis;
	
	public int BFS(int v) {
		Queue<Integer> queue=new LinkedList<>();
		int answer=0;
		ch[v]=1;
		dis[v]=0;
		queue.offer(v);
		while(!queue.isEmpty()) {
			int cv=queue.poll();
			for(int nv:graph.get(cv)) {
				if(ch[nv]==0) {
					ch[nv]=1;
					queue.offer(nv);
					dis[nv]=dis[cv]+1;
					answer++;
				}
			}
		}
		
		return answer;
	}
	
	public static void main(String[] args) {
		Main T=new Main();
		Scanner sc=new Scanner(System.in);
		int numCom=sc.nextInt();
		int line=sc.nextInt();
		graph=new ArrayList<ArrayList<Integer>>();
		for(int i = 0;i<=numCom;i++) {
			graph.add(new ArrayList<Integer>());
		}
		ch=new int[numCom+1];
		dis=new int[numCom+1];
		for(int i = 0;i<line;i++) {
			int a=sc.nextInt();
			int b=sc.nextInt();
			graph.get(a).add(b);
			graph.get(b).add(a);
		}
		System.out.println(T.BFS(1));
		
		
	}

}
