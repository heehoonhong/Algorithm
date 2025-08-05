//package ctp;

import java.io.*;
import java.util.*;
import java.util.Arrays;

public class Main {	
	
	public static class Point{
		int x;
		int y;
		Point(int x,int y){
			this.x=x;
			this.y=y;
		}
	}
	
	public static int[][] iceMap;
	public static int numRow,numCol;
	public static int numDays;
	public static int[] dx= {0,0,-1,1};
	public static int[] dy= {-1,1,0,0};
	public static BufferedWriter bw;
	
	// 얼음인 위치를 담을 Queue
	public static Queue<Point> queue=new LinkedList<>();
	
	// 그룹이 얼마나 있는지를 알기 위해 필요한 Queue
	public static Queue<Point> groupQueue=new LinkedList<>();
	
	// 그룹의 개수를 알기 위해 필요한 visited 배열
	public static int[][] visited;
	
	public static int[][] decreaseIce;
	
    public static void main(String[] args) throws Exception {    	
    	BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
    	bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	StringTokenizer st=new StringTokenizer(br.readLine());
    	
    	numRow=Integer.parseInt(st.nextToken());
    	numCol=Integer.parseInt(st.nextToken());
    	
    	iceMap=new int[numRow][numCol];
    	decreaseIce=new int[numRow][numCol];
    	
    	visited=new int[numRow][numCol];
    	
    	for(int i = 0;i<numRow;i++) {
    		st=new StringTokenizer(br.readLine());
    		for(int j = 0;j<numCol;j++) {
    			iceMap[i][j]=Integer.parseInt(st.nextToken());
    			if(iceMap[i][j]!=0) {
    				queue.offer(new Point(i,j));
    			}
    		}
    	}
    	numDays=0;
    	// 여기까지가 입력 부분 아래부터 구현해야 함.
    	
    	// bfs 하기 전에 0이 아닌 포인트 값을 큐에 넣어두면 편할 듯
    	
    	bfs();
    	
    	bw.write(numDays+"\n");
    	
    	br.close();
    	bw.flush();
    	bw.close();
    }
    
    public static void bfs() throws IOException {
    	
    	while(true) {
    		int size=queue.size();
    		int[][] melt=new int[numRow][numCol];
    		for(int k=0;k<size;k++) {
    			Point point=queue.poll();
    			melt[point.x][point.y]=howManyIcesNearHere(point);
    		}
    		
    		for(int i = 0;i<numRow;i++) {
    			for(int j = 0;j<numCol;j++) {
    				if(iceMap[i][j]>0) {
    					iceMap[i][j]=Math.max(0, iceMap[i][j]-melt[i][j]);
    				}
    			}
    		}
    		
    		for (int i = 0; i < numRow; i++) {
                for (int j = 0; j < numCol; j++) {
                    if (iceMap[i][j] > 0) {
                        queue.offer(new Point(i, j));
                    }
                }
            }
    		numDays++;
            // 이하 군집 검사 → 종료/증가 로직...
            int groups = detectTwoMoreSeparate();
            if (groups >= 2) break;
            if (queue.isEmpty()) { numDays = 0; break; }
            
    	}
    }
    
    public static int howManyIcesNearHere(Point point) {
    	int numIces=0;
    	// dx, dy 배열을 통해 동서남북의 얼음 개수를 세서 리턴하기
    	for(int i = 0;i<4;i++) {
    		int nx=point.x+dx[i];
    		int ny=point.y+dy[i];
    		if(nx>=0&&nx<numRow&&ny>=0&&ny<numCol) {// 경계에 있고
    			if(iceMap[nx][ny]==0) { // 이 위치에 얼음이 있다면
    				numIces++;
    			}
    			
    		}
    	}
    	return numIces;
    }
    
    public static int detectTwoMoreSeparate() throws IOException {
    	
    	// 방문 기록 초기화
        for (int i = 0; i < numRow; i++) {
            Arrays.fill(visited[i], 0);
        }
        groupQueue.clear();
    	
    	int numGroups=0;
    	
    	
    	// 이중 for문을 통해 전체적으로 for문을 돌면서 BFS 탐색을 진행
    	// 얼음이 있다면(iceMap[i][j]!=0)이라면 groupQueue에 넣고,
    	// 그 포인트에 대해서 BFS 탐색을 진행
    	for(int i = 0;i<numRow;i++) {
    		for(int j = 0;j<numCol;j++) {
    			// 군집 발견한 것이므로
    			// groupQueue에 넣고, numGroups 증가시키기
    			// 그리고 bfs 탐색 진행
    			// 그리고 방문 처리도 해야지
    			if(visited[i][j]==0&&iceMap[i][j]!=0) {
    				numGroups++;
    				groupQueue.offer(new Point(i,j));
    				visited[i][j]=1;
    				
    				while(!groupQueue.isEmpty()) {
    					// 꺼내고 방문처리하기
    					Point point=groupQueue.poll();
    					visited[point.x][point.y]=1;
    					for(int dir=0;dir<4;dir++) {
    						int nx=point.x+dx[dir];
    						int ny=point.y+dy[dir];
    						if(nx>=0&&nx<numRow&&ny>=0&&ny<numCol) {
    							if(iceMap[nx][ny]!=0&&visited[nx][ny]==0) {
    								visited[nx][ny]=1;
    								groupQueue.offer(new Point(nx,ny));
    							}
    						}
    					}
    				}
    				
    				
    			}
    		}
    	}
    	//bw.write(numGroups+"\n");
    	return numGroups;
    }
    
    
}
