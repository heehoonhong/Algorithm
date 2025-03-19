//package ctp;

import java.io.*;
import java.util.*;

class Point{
	int x,y,z;
	Point(int x,int y,int z){
		this.x=x;
		this.y=y;
		this.z=z;
	}
}


public class Main {
	
	static int[][][] graph;
	static int[][][] visited;
	
	static int[] dx= {-1,1,0,0,0,0};
	static int[] dy= {0,0,-1,1,0,0};
	static int[] dz= {0,0,0,0,-1,1};
	static Queue<Point> queue=new LinkedList<>();
	static int m,n,h;
	
	public static void BFS() {
		while(!queue.isEmpty()) {
			Point temp=queue.poll();
			visited[temp.x][temp.y][temp.z]=1;
			for(int i = 0;i<6;i++) {
				int nx=temp.x+dx[i];
				int ny=temp.y+dy[i];
				int nz=temp.z+dz[i];
				if(nx>=1&&nx<=h&&ny>=1&&ny<=n&&nz>=1&&nz<=m) {
					if(graph[nx][ny][nz]==0&&visited[nx][ny][nz]==0) {
						queue.offer(new Point(nx,ny,nz));
						visited[nx][ny][nz]=1;
						graph[nx][ny][nz]=graph[temp.x][temp.y][temp.z]+1;
					}
					
				}
			}
		}
	}
	
	
    public static void main(String[] args) throws Exception {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	String line=br.readLine();
    	StringTokenizer st=new StringTokenizer(line);
    	m=Integer.parseInt(st.nextToken());
    	n=Integer.parseInt(st.nextToken());
    	h=Integer.parseInt(st.nextToken());
    	
    	graph=new int[h+1][n+1][m+1];
    	visited=new int[h+1][n+1][m+1];
    	
    	
    	
    	for(int i = 1;i<=h;i++) {
    		for(int j=1;j<=n;j++) {
    			String l=br.readLine();
    			st=new StringTokenizer(l);
    			for(int k=1;k<=m;k++) {
    				graph[i][j][k]=Integer.parseInt(st.nextToken());
    				if(graph[i][j][k]==1) {
    					queue.offer(new Point(i,j,k));
    				}
    			}
    		}
    	}
    	BFS();
    	int maxNum=Integer.MIN_VALUE;
    	for(int i=1;i<=h;i++) {
    		for(int j = 1;j<=n;j++) {
    			for(int k=1;k<=m;k++) {
    				if(graph[i][j][k]==0) {
    					bw.write(-1+"\n");
    					br.close();
    			    	bw.flush();
    			    	bw.close();
    					return;
    				}
    				if(maxNum<graph[i][j][k]) {
    					maxNum=graph[i][j][k];
    				}
    			}
    		}
    	}
    	
    	bw.write(maxNum-1+"\n");
    	
    	br.close();
    	bw.flush();
    	bw.close();
    }
}
