//package ctp;

import java.io.*;
import java.util.*;

public class Main {
   
   public static class Point{
      int x,y;
      Point(int x,int y){
         this.x=x;
         this.y=y;
      }
   }

   public static int rowNum,colNum;
   public static int[][] map;
   public static int startRow,startCol,startDirection;
   public static Point[] vectorList;
   public static int cleanCount;
   public static int[] dx= {-1,1,0,0};
   public static int[] dy= {0,0,-1,1};
   
   public static void main(String[] args) throws Exception {
      BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
      BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
      
      cleanCount=0;
      
      StringTokenizer st=new StringTokenizer(br.readLine());
      rowNum=Integer.parseInt(st.nextToken());
      colNum=Integer.parseInt(st.nextToken());
      
      st=new StringTokenizer(br.readLine());
      
      startRow=Integer.parseInt(st.nextToken());
      startCol=Integer.parseInt(st.nextToken());
      startDirection=Integer.parseInt(st.nextToken());
      
      map=new int[rowNum][colNum];
      
      for(int i = 0;i<rowNum;i++) {
         st=new StringTokenizer(br.readLine());
         for(int j = 0;j<colNum;j++) {
            map[i][j]=Integer.parseInt(st.nextToken());
         }
      }
      
      vectorList=new Point[4];
      
      vectorList[0]=new Point(-1,0);
      vectorList[1]=new Point(0,1);
      vectorList[2]=new Point(1,0);
      vectorList[3]=new Point(0,-1);
      
      cleanRobot(new Point(startRow,startCol),vectorList,startDirection);
      
      bw.write(cleanCount+"\n");
      
      br.close();
      bw.flush();
      bw.close();
   }
   
   public static void cleanRobot(Point p,Point[] vectorList,int startDirection) {
      int x=p.x;
      int y=p.y;
      int dir=startDirection;
      
      while(true) {
    	  // 1. 현재 칸 청소
    	  if(inRange(x,y)&&map[x][y]==0) {
    		  map[x][y]=2;
    		  cleanCount++;
    	  }
    	  
    	  boolean moved=false;
    	  for(int i = 0;i<4;i++) {
    		  dir=(dir+3)%4;
    		  int nx=x+vectorList[dir].x;
    		  int ny=y+vectorList[dir].y;
    		  
    		  if(inRange(nx,ny)&&map[nx][ny]==0) {
    			  x=nx;
    			  y=ny;
    			  moved=true;
    			  break;
    		  }
    	  }
    	  
    	  if(moved) continue;
    	  
    	  // moved가 true 라면
    	  // continue니까 아래 코드는 실행되지 않고,
    	  // false, 즉 움직일 수 없는 경우의 코드임
    	  
    	  // 네 방향 모두 못 갈 때
    	  int bx=x-vectorList[dir].x;
    	  int by=y-vectorList[dir].y;
    	  
    	  if(!inRange(bx,by)||map[bx][by]==1) {
    		  return;
    	  }
    	  else {
    		  
    		  // 후진만 하고 방향은 유지한다.
    		  x=bx;
    		  y=by;
    	  }
    	  
      }
      
   }
   
   public static boolean inRange(int x,int y) {
	   if(x>=0&&x<rowNum&&y>=0&&y<colNum) {
		   return true;
	   }
	   else {
		   return false;
	   }
   }
   
   public static Queue<Point> detectNearClean(Point p) {
	   Queue<Point> queue=new LinkedList<>();
	   for(int i = 0;i<vectorList.length;i++) {
		   // 청소되지 않은 빈칸이라면
		   if(map[p.x+vectorList[i].x][p.y+vectorList[i].y]==0) {
			   // 벡터를 저장하기
			   queue.offer(vectorList[i]);
		   }
	   }
	   return queue;
   }
   
   // 후진 가능한지 참 거짓만 반환해주는 함수
   public static boolean canBackward(Point p,Point vector) {
	   // 벽이 아니라면 후진 가능
	   if(map[p.x-vector.x][p.y-vector.y]!=1) { 
		   return true;
	   }
	   else {
		   return false;
	   }
   }
   
   public static boolean currentSpaceNotCleaned(Point p) {
      // 빈 칸도 아니고 벽도 아니라면 
      
      if(map[p.x][p.y]!=0 && map[p.x][p.y]!=1) {
         return true;
      }
      else {
         return false;
      }
   }

}

