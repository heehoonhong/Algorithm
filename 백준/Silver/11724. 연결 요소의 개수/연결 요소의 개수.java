//package ctp;

import java.io.*;
import java.util.*;



public class Main {
    
	static int[][] graph;
	static int[] visited;
	static int n,m;
	
	public static void DFS(int v) {
		visited[v]=1;
		for(int i = 1;i<=n;i++) {
			if(visited[i]!=1&&graph[v][i]==1) {
				DFS(i);
			}
		}
	}
	
    public static void main(String[] args) throws Exception {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	String line=br.readLine();
    	StringTokenizer st=new StringTokenizer(line);
    	n=Integer.parseInt(st.nextToken());
    	m=Integer.parseInt(st.nextToken());
    	
    	graph=new int[n+1][n+1];
    	visited=new int[n+1];
    	
    	for(int i = 0;i<m;i++) {
    		String l=br.readLine();
    		st=new StringTokenizer(l);
    		int u=Integer.parseInt(st.nextToken());
    		int v=Integer.parseInt(st.nextToken());
    		graph[u][v]=1;
    		graph[v][u]=1;
    	}
    	
    	int count=0;
    	for(int i = 1;i<=n;i++) {
    		if(visited[i]!=1) {
    			DFS(i);
    			count++;
    		}
    	}
    	bw.write(count+"\n");
    	
    	br.close();
    	bw.flush();
    	bw.close();
    }
}
