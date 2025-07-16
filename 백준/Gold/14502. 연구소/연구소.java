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
	
	public static int[][] graph;
	public static int[][] visited;
	public static int safetyNum;
	public static int[] dx= {1,-1,0,0};
	public static int[] dy= {0,0,-1,1};
	public static Queue<Point> queue=new LinkedList<>();
	public static int rowNum,colNum;
	public static int maxCount;
	public static BufferedWriter bw;
	
	// 0 빈칸, 1 벽, 2 바이러스
    public static void main(String[] args) throws Exception {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	String line=br.readLine();
    	StringTokenizer st=new StringTokenizer(line);
    	
    	rowNum=Integer.parseInt(st.nextToken());
    	colNum=Integer.parseInt(st.nextToken());
    	
    	graph=new int[rowNum][colNum];
    	visited=new int[rowNum][colNum];
    	
    	maxCount=0;
    	
    	List<Point> empties=new ArrayList<>();
    	for(int i = 0;i<rowNum;i++) {
    		line=br.readLine();
    		st=new StringTokenizer(line);
    		for(int j = 0;j<colNum;j++) {
    			graph[i][j]=Integer.parseInt(st.nextToken());
    			if(graph[i][j]==2) {
    				queue.offer(new Point(i,j));
    			}
    			else if(graph[i][j]==0) {
    				empties.add(new Point(i,j));
    			}
    		}
    	}
    	
    	int n=empties.size();
    	for(int a=0;a<n-2;a++) {
    		for(int b=a+1;b<n-1;b++) {
    			for(int c=b+1;c<n;c++) {
    				Point w1=empties.get(a);
    				Point w2=empties.get(b);
    				Point w3=empties.get(c);
    			
    				graph[w1.x][w1.y]=1;
    				graph[w2.x][w2.y]=1;
    				graph[w3.x][w3.y]=1;
    				
    				int safe=bfs();
    				maxCount=Math.max(maxCount,safe);
    				
    				graph[w1.x][w1.y]=0;
    				graph[w2.x][w2.y]=0;
    				graph[w3.x][w3.y]=0;
    			}
    		}
    	}
    	
    	
    	
    	
    	
    	bw.write(maxCount+"\n");
    	
    	br.close();
    	bw.flush();
    	bw.close();
    }
    
    
    
    // 바이러스 증가
    public static int bfs() {
    	
    	// visited 초기화 & 전체 빈칸 개수 세기
    			int totalZeros = 0;
    			for (int i = 0; i < rowNum; i++) {
    				for (int j = 0; j < colNum; j++) {
    					visited[i][j] = 0;
    					if (graph[i][j] == 0) totalZeros++;
    				}
    			}

    			// 로컬 큐에 바이러스 시작점
    			Queue<Point> localQ = new LinkedList<>(queue);
    			for (Point p : localQ) {
    				visited[p.x][p.y] = 1;
    			}

    			// BFS 전파 및 감염된 칸 수 세기
    			int infected = 0;
    			while (!localQ.isEmpty()) {
    				Point p = localQ.poll();
    				for (int d = 0; d < 4; d++) {
    					int nx = p.x + dx[d];
    					int ny = p.y + dy[d];
    					if (nx >= 0 && nx < rowNum
    					 && ny >= 0 && ny < colNum
    					 && visited[nx][ny] == 0
    					 && graph[nx][ny] == 0) {
    						
    						visited[nx][ny] = 1;
    						infected++;
    						localQ.offer(new Point(nx, ny));
    					}
    				}
    			}

    			return totalZeros - infected;
    		}
}
