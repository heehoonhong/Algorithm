//package ctp;

import java.io.*;
import java.util.*;

public class Main {	
	
	public static class Point{
		int x;
		int y;
		Point(int x,int y){
			this.x=x;
			this.y=y;
		}
	}
	
	public static int rowNum,minNum,maxNum;
	public static int[][] map;
	public static int[][] visited;
	public static Queue<Point> queue=new LinkedList<>();
	public static ArrayList<Point> arrayList=new ArrayList<>();
	public static boolean isMove;
	public static int[] dx= {-1,1,0,0};
	public static int[] dy= {0,0,-1,1};
	public static int count=0;
	
    public static void main(String[] args) throws Exception {    	
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	String line=br.readLine();
    	StringTokenizer st=new StringTokenizer(line);
    	
    	rowNum=Integer.parseInt(st.nextToken());
    	minNum=Integer.parseInt(st.nextToken());
    	maxNum=Integer.parseInt(st.nextToken());
    	map=new int[rowNum][rowNum];
    	visited=new int[rowNum][rowNum];
    	
    	for(int i = 0;i<rowNum;i++) {
    		line=br.readLine();
    		st=new StringTokenizer(line);
    		for(int j=0;j<rowNum;j++) {
    			map[i][j]=Integer.parseInt(st.nextToken());
    		}
    	}
    	
    	move();
    	
    	bw.write(count+"\n");
    	
    	br.close();
    	bw.flush();
    	bw.close();
    }
    
    public static void move() {
    	while(true) {
    		isMove=false;
    		visited=new int[rowNum][rowNum];
    		for(int i = 0;i<rowNum;i++) {
    			for(int j = 0;j<rowNum;j++) {
    				if(visited[i][j]==0) {
    					bfs(i,j);
    				}
    			}
    		}
    		if(!isMove) {
    			break;
    		}
    		else {
    			count++;
    		}
    	}
    }
    
    public static void bfs(int x, int y) {
    	queue.offer(new Point(x,y));
    	arrayList.add(new Point(x,y));
    	while(!queue.isEmpty()) {
    		Point point=queue.poll();
    		visited[point.x][point.y]=1;
    		for(int i = 0;i<4;i++) {
    			int nx=dx[i]+point.x;
    			int ny=dy[i]+point.y;
    			if(nx>=0&&nx<rowNum&&ny>=0&&ny<rowNum&&visited[nx][ny]==0) {
    				// 거리가 minNum,maxNum 사이라면
    				int distance=Math.abs(map[point.x][point.y]-map[nx][ny]);
    				if(distance>=minNum&&distance<=maxNum) {
    					isMove=true;
    					visited[nx][ny]=1;
    					queue.offer(new Point(nx,ny));
    					arrayList.add(new Point(nx,ny));
    				}
    			}
    		}
    	}
    	
    	// 인구이동을 한다.
    	// 인구이동은 총 인구 수/리스트의 사이즈로 해서 공평하게 나눈다.
    	int sum=0;
    	for(int i = 0;i<arrayList.size();i++) {
    		Point point=arrayList.get(i);
    		sum+=map[point.x][point.y];
    	}
    	for(int i = 0;i<arrayList.size();i++) {
    		Point point=arrayList.get(i);
    		map[point.x][point.y]=sum/arrayList.size();
    	}
    	arrayList.removeAll(arrayList);
    	
    }
    
    
}
