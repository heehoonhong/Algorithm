//package ctp;

import java.util.*;

class Point{
	public int x,y;
	Point(int x,int y){
		this.x=x;
		this.y=y;
	}
}


public class Main {
	
	static int[] dx= {-1,0,1,0};
	static int[] dy= {0,1,0,-1};
	static int[][]visited,dis;
	static int n,m;
	
    public int BFS(int x,int y) {
    	//int answer=0;
    	Queue<Point> queue=new LinkedList<>();
    	queue.offer(new Point(x,y));
    	visited[x][y]=1;
    	
    	while(!queue.isEmpty()) { // next Point를 찾기 위한 과정
    		Point temp=queue.poll();
    		for(int i = 0;i<4;i++) {
    			int nx=temp.x+dx[i];
    			int ny=temp.y+dy[i];
    			if(nx>=1&&nx<=n&&ny>=1&&ny<=m&&visited[nx][ny]==0&&dis[nx][ny]==1) {
    				queue.offer(new Point(nx,ny));
    				dis[nx][ny]=dis[temp.x][temp.y]+1;
    				visited[nx][ny]=1;
    			}
    		}
    	}
    	
    	return dis[n][m];
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        n=sc.nextInt();
        m=sc.nextInt();
        dis= new int[n+1][m+1];
        visited=new int[n+1][m+1];
        for(int i = 1;i<=n;i++) {
        	String line=sc.next();
        	for(int j = 1;j<=m;j++) {
        		dis[i][j]=line.charAt(j-1)-'0';
        	}
        }
        System.out.println(T.BFS(1,1));
    }
}
