import java.util.*;
import java.io.*;

class Solution {
    
    public static class Point{
        int x,y;
        
        Point(int x,int y){
            this.x=x;
            this.y=y;
        }
    }
    
    public static int[] dx={-1,1,0,0};
    public static int[] dy={0,0,-1,1};
    public static int[][] visited;
    public static int answer;
    public static int n,m;
    public static Queue<Point> queue=new LinkedList<>();
    public int solution(int[][] maps) {
        answer = 0;
        
        // 방문 배열 초기화
        visited=new int[maps.length][maps[0].length];
        
        bfs(maps);
        
        if(visited[n-1][m-1]!=0){
            return visited[n-1][m-1];
        }
        else{
            return -1;
        }
        
        //return answer;
    }
    
    public static void bfs(int[][] maps){
        n=maps.length;
        m=maps[0].length;
        
        queue.offer(new Point(0,0));
        visited[0][0]=1;
        
        while(!queue.isEmpty()){
            Point p=queue.poll();
            for(int i=0;i<4;i++){
                int nx=p.x+dx[i];
                int ny=p.y+dy[i];
                if(nx>=0&&nx<n&&ny>=0&&ny<m){ // 주어진 범위 안에 있고
                    if(visited[nx][ny]==0&&maps[nx][ny]==1){
                        queue.offer(new Point(nx,ny));
                        visited[nx][ny]+=visited[p.x][p.y]+1;
                        //answer++;
                    }
                }
            }
        }
        
    }
}