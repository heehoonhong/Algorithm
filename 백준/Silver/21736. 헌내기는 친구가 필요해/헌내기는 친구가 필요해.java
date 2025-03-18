//package ctp;

import java.io.*;
import java.util.*;

class Point{
	int x,y;
	Point(int x,int y){
		this.x=x;
		this.y=y;
	}
}


public class Main {
    
	static char[][] graph;
	static int[][] visited;
	static int[] dx= {-1,1,0,0};
	static int[] dy= {0,0,-1,1};
	static Queue<Point> queue=new LinkedList<>();
	static int n,m;
	static BufferedWriter bw;
	
	public static void BFS() throws Exception {
		int count=0;
		
		
		while(!queue.isEmpty()) {
			Point temp=queue.poll();
			visited[temp.x][temp.y]=1; // 방문 처리
			for(int i = 0;i<4;i++) {
				int nx=temp.x+dx[i];
				int ny=temp.y+dy[i];
				if(nx>=1&&nx<=n&&ny>=1&&ny<=m&&visited[nx][ny]==0&&!(graph[nx][ny]=='X')) {
					queue.offer(new Point(nx,ny));
					visited[nx][ny]=1;
					if(graph[nx][ny]=='P') {
						
						count++;
					}
				}
			}
		}
		if(count>=1) {
			bw.write(count+"\n");
		}
		else {
			bw.write("TT\n");
		}
		
	}
	
    public static void main(String[] args) throws Exception {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	String line=br.readLine();
    	StringTokenizer st=new StringTokenizer(line);
    	n=Integer.parseInt(st.nextToken());
    	m=Integer.parseInt(st.nextToken());
    	
    	graph=new char[n+1][m+1];
    	visited=new int[n+1][m+1];
    	
    	for(int i = 1;i<=n;i++) {
    		String l=br.readLine();
    		char[] arr=l.toCharArray();
    		for(int j = 1;j<=m;j++) {
    			graph[i][j]=arr[j-1];
    		}
    	}
    	
    	for(int i = 1;i<=n;i++) {
    		for(int j = 1;j<=m;j++) {
    			if(graph[i][j]=='I') {
    				queue.offer(new Point(i,j));
    			}
    		}
    	}
    	BFS();
    	
    	br.close();
    	bw.flush();
    	bw.close();
    }
}
