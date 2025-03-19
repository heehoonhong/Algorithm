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
	
	static int n;
	static char[][] graph;
	static int[][] visited;
	static int[] dx= {-1,1,0,0};
	static int[] dy= {0,0,-1,1};
	static Queue<Point> queue=new LinkedList<>();
	
	public static void BFS(int x,int y) {
		if(visited[x][y]==0) queue.offer(new Point(x,y));
		while(!queue.isEmpty()) {
			Point temp=queue.poll();
			visited[temp.x][temp.y]=1;
			for(int i = 0;i<4;i++) {
				int nx=temp.x+dx[i];
				int ny=temp.y+dy[i];
				if(nx>=1&&nx<=n&&ny>=1&&ny<=n) {
					if(graph[nx][ny]==graph[temp.x][temp.y]&&visited[nx][ny]==0) {
						visited[nx][ny]=1;
						queue.offer(new Point(nx,ny));
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
		n=Integer.parseInt(line);
		graph=new char[n+1][n+1];
		visited=new int[n+1][n+1];
		
		for(int i = 1;i<=n;i++) {
			char[] arr=br.readLine().toCharArray();
			for(int j = 1;j<=n;j++) {
				graph[i][j]=arr[j-1];
			}
		}
		
		int count=0;
		for(int i = 1;i<=n;i++) {
			for(int j = 1;j<=n;j++) {
				if(visited[i][j]==0) {
					BFS(i,j);
					count++;
				}
			}
		}
		
		visited=new int[n+1][n+1];
		for(int i = 1;i<=n;i++) {
			for(int j = 1;j<=n;j++) {
				if(graph[i][j]=='G'||graph[i][j]=='R') {
					graph[i][j]='K';
				}
			}
		}
		
		int countS=0;
		for(int i = 1;i<=n;i++) {
			for(int j = 1;j<=n;j++) {
				if(visited[i][j]==0) {
					BFS(i,j);
					countS++;
				}
			}
		}
		
		
		bw.write(count+" ");
		bw.write(countS+"\n");
		br.close();
		bw.flush();
		bw.close();
    }
}
