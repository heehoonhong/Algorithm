//package ctp;

import java.io.*;
import java.util.*;

public class Main {	
	
	static class Node{
		int x,y,broke,distance;
		Node(int x,int y,int broke,int distance){
			this.x=x;
			this.y=y;
			this.broke=broke;
			this.distance=distance;
		}
	}
	
	public static int rowNum,colNum;
	public static int[][] graph;
	public static int[][][] visited;
	public static int minDistance;
	public static int[] dx= {-1,1,0,0};
	public static int[] dy= {0,0,-1,1};
	public static BufferedWriter bw;
	
    public static void main(String[] args) throws Exception {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	String line=br.readLine();
    	StringTokenizer st=new StringTokenizer(line);
    	
    	rowNum=Integer.parseInt(st.nextToken());
    	colNum=Integer.parseInt(st.nextToken());
    	
    	graph=new int[rowNum][colNum];
    	visited=new int[rowNum][colNum][2];
    	
    	minDistance=Integer.MAX_VALUE;
    	
    	for(int i =0;i<rowNum;i++) {
    		line=br.readLine();
    		char[] lineArr=line.toCharArray();
    		for(int j = 0;j<colNum;j++) {
    			graph[i][j]=(int)(lineArr[j]-'0');
    		}
    	}
    	
    	
    	bfs();
    	
    	if(minDistance==Integer.MAX_VALUE) {
    		bw.write("-1\n");
    	}
    	else {
    		bw.write(minDistance+"\n");
    	}
    	
    	br.close();
    	bw.flush();
    	bw.close();
    }
    
    public static void bfs() {
    	Queue<Node> queue=new LinkedList<>();
    	
    	visited[0][0][0]=1; // 방문 처리
    	queue.offer(new Node(0,0,0,1));
    	while(!queue.isEmpty()) {
    		
    		Node node=queue.poll();
    		int x=node.x;
    		int y=node.y;
    		int broke=node.broke;
    		int distance=node.distance;
    		
    		// 도착했을 때
    		if(x==rowNum-1&&y==colNum-1) {
    			minDistance=distance;
    			return;
    		}
    		
    		for(int i = 0;i<4;i++) {
    			int nx=x+dx[i];
    			int ny=y+dy[i];
    			if(nx>=0&&nx<rowNum&&ny>=0&&ny<colNum) {
    				
    				// 방문하지 않은, 빈 칸이라면
    				if(visited[nx][ny][broke]==0&&graph[nx][ny]==0) {
    					visited[nx][ny][broke]=1;
    					queue.offer(new Node(nx,ny,broke,distance+1));
    				}
    				// 벽인데, 아직 안 뚫었다면, 당연히 방문도 안 했어야지
    				else if(graph[nx][ny]==1&&broke==0&&visited[nx][ny][1]==0) {
    					visited[nx][ny][1]=1;
    					queue.offer(new Node(nx,ny,1,distance+1));
    				}
    			}
    		}
    	}
    }
    
}
