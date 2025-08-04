//package ctp;

import java.io.*;
import java.util.*;

public class Main {	
	
	public static class Node{
		int location;
		int time;
		Node(int location,int time){
			this.location=location;
			this.time=time;
		}
	}
	
	public static int subinLocation,brotherLocation;
	public static Queue<Node> queue=new LinkedList<>();
	public static int resultTime=Integer.MAX_VALUE;
	public static int[] visited=new int[100001];
	public static int maxNum=100000;
	public static int minTime=Integer.MAX_VALUE;
	public static BufferedWriter bw;
	
    public static void main(String[] args) throws Exception {    	
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	String line=br.readLine();
    	StringTokenizer st=new StringTokenizer(line);
    	
    	subinLocation=Integer.parseInt(st.nextToken());
    	brotherLocation=Integer.parseInt(st.nextToken());
    	
    	queue.offer(new Node(subinLocation,0));
    	visited[subinLocation] = 1;
    	
    	bfs();
    	
    	bw.write(minTime+"\n");
    	
    	br.close();
    	bw.flush();
    	bw.close();
    }
    
    public static void bfs() throws IOException {
    	while(!queue.isEmpty()) {
    		// 꺼내서 방문 처리하기
    		Node node=queue.poll();
    		visited[node.location]=1;
    		
    		if(node.location==brotherLocation) {
    			minTime=Math.min(minTime, node.time);
    			return;
    		}
    		
    		if(node.location*2<=maxNum&&visited[node.location*2]==0) {
    			//visited[node.location *2] = 1;
    			queue.offer(new Node(node.location*2,node.time));
    		}
    		
    		if(node.location-1>=0&&visited[node.location-1]==0) {
    			//visited[node.location - 1] = 1;
    			queue.offer(new Node(node.location-1,node.time+1));
    		}
    		
    		if(node.location+1<=maxNum&&visited[node.location+1]==0) {
    			//bw.write(node.location+"\n");
    			//visited[node.location + 1] = 1;
    			queue.offer(new Node(node.location+1,node.time+1));
    		}
    		
    		
    	}
    }
}
