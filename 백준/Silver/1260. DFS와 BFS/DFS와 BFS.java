//package ctp;

import java.io.*;
import java.util.*;



public class Main {
    
	static int[][] graph;
	static int[] visited;
	static int n,m,v;
	static BufferedWriter bw;
	static Queue<Integer> queue=new LinkedList<>();
	
	public static void DFS(int v) throws Exception {
		visited[v]=1;
		bw.write(v+" ");
		for(int i = 1;i<=n;i++) {
			if(visited[i]!=1&&graph[v][i]==1) {
				DFS(i);
			}
		}
	}
	
	public static void BFS() throws Exception{
		
		while(!queue.isEmpty()) {
			// 꺼내고 출력하기
			int v=queue.poll();
			bw.write(v+" ");
			for(int i = 1;i<=n;i++) {
				if(visited[i]!=1&&graph[v][i]==1) {
					visited[i]=1;
					queue.offer(i);
				}
			}
		}
	}
	
    public static void main(String[] args) throws Exception {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	String line=br.readLine();
    	StringTokenizer st=new StringTokenizer(line);
    	
    	n=Integer.parseInt(st.nextToken());
    	m=Integer.parseInt(st.nextToken());
    	v=Integer.parseInt(st.nextToken());
    	
    	graph=new int[n+1][n+1];
    	visited=new int[n+1];
    	
    	for(int i = 0;i<m;i++) {
    		String l=br.readLine();
    		st=new StringTokenizer(l);
    		
    		int a=Integer.parseInt(st.nextToken());
    		int b=Integer.parseInt(st.nextToken());
    		
    		graph[a][b]=1;
    		graph[b][a]=1;
    	}
    	
    	DFS(v);
    	bw.write("\n");
    	for(int i = 1;i<=n;i++) {
    		visited[i]=0;
    	}
    	
    	visited[v]=1;
    	queue.offer(v);
    	BFS();
    	bw.write("\n");
    
    	br.close();
    	bw.flush();
    	bw.close();
    }
}
