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
	
	static int[][] graph;
	static int[][] visited;
	static int[][] dis;
	static int[] dx= {-1,1,0,0};
	static int[] dy= {0,0,-1,1};
	static Queue<Point> queue=new LinkedList<>();
	static int n,m;
	
	public static void BFS() {
		while(!queue.isEmpty()) {
			Point temp=queue.poll();
			visited[temp.x][temp.y]=1;
			for(int i=0;i<4;i++) {
				int nx=temp.x+dx[i];
				int ny=temp.y+dy[i];
				if(nx>=1&&nx<=n&&ny>=1&&ny<=m&&visited[nx][ny]==0&&graph[nx][ny]!=0) {
					queue.offer(new Point(nx,ny));
					visited[nx][ny]=1;
					dis[nx][ny]=dis[temp.x][temp.y]+1;
				}
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
    	
    	graph=new int[n+1][m+1];
    	visited=new int[n+1][m+1];
    	dis=new int[n+1][m+1];
    	
    	for(int i = 1;i<=n;i++) {
    		String l=br.readLine();
    		st=new StringTokenizer(l);
    		for(int j = 1;j<=m;j++) {
    			graph[i][j]=Integer.parseInt(st.nextToken());
    		}
    	}
    	
    	for(int i = 1;i<=n;i++) {
    		for(int j = 1;j<=m;j++) {
    			if(graph[i][j]==2) {
    				queue.offer(new Point(i,j));
    			}
    		}
    	}
    	
    	BFS();
    	for(int i = 1;i<=n;i++) {
    		for(int j = 1;j<=m;j++) {
    			if(graph[i][j]==2) {
    				bw.write(0+" ");
    			}
    			else {
    				if(graph[i][j]==0) {
        				bw.write(0+" ");
        			}
        			else {
        				if(dis[i][j]==0) {
        					bw.write(-1+" ");
        				}
        				else {
        					bw.write(dis[i][j]+" ");
        				}
        			}
    			}
    		}
    		bw.write("\n");
    	}
    	
    	br.close();
    	bw.flush();
    	bw.close();
    }
}
