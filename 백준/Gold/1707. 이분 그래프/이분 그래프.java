//package ctp;

import java.io.*;
import java.util.*;

public class Main {	
	
	
	public static int[] visited;
	public static ArrayList<Integer>[] arrayList;
	
    public static void main(String[] args) throws Exception {    	
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	int numTestcases=Integer.parseInt(br.readLine());
    	
    	StringTokenizer st;
    	for(int tc = 0;tc<numTestcases;tc++) {
    		st=new StringTokenizer(br.readLine());
    		int numVertices=Integer.parseInt(st.nextToken());
    		int numEdges=Integer.parseInt(st.nextToken());
    		
    		// 초기화
    		visited=new int[numVertices+1];
    		arrayList=new ArrayList[numVertices+1];
    		for(int i = 1;i<=numVertices;i++) {
    			arrayList[i]=new ArrayList<>();
    		}
    		
    		for(int i = 0;i<numEdges;i++) {
    			st=new StringTokenizer(br.readLine());
    			int u=Integer.parseInt(st.nextToken());
    			int v=Integer.parseInt(st.nextToken());
    			arrayList[u].add(v);
    			arrayList[v].add(u);
    		}
    		
    		boolean isBipartite=true;
    		for(int v=1;v<=numVertices;v++) {
    			if(visited[v]==0) {
    				visited[v]=1;
    				boolean canBi=bfs(v);
    				if(!canBi) {
    					bw.write("NO\n");
    					isBipartite=false;
    					break;
    				}
    				else {
    					//bw.write("YES\n");
    				}
    			}
    		}
    		if (isBipartite) {
    			   			bw.write("YES\n");
    		}
    	}
    	
    	
    	
    	br.close();
    	bw.flush();
    	bw.close();
    }
    
    public static boolean bfs(int start) {
    	Queue<Integer> queue=new LinkedList<>();
    	queue.offer(start);
    	
    	while(!queue.isEmpty()) {
    		int u=queue.poll();
    		for(int v:arrayList[u]) {
    			if(visited[v]==0) {
    				visited[v]=-visited[u];
    				queue.offer(v);
    			}
    			else if(visited[v]==visited[u]) {
    				return false;
    			}
    			else {
    				
    			}
    		}
    	}
    	
    	return true;
    }
}
