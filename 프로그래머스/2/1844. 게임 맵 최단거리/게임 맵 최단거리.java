import java.util.*;

class Solution {
    public static int n,m;
    public static int[][] visited;
    public static int[] dx={-1,1,0,0};
    public static int[] dy={0,0,1,-1};
    
    public static class Point{
        int x;
        int y;
        public Point(int x,int y){
            this.x=x;
            this.y=y;
        }
    }
    public static void bfs(int x,int y,int [][] maps){
        Queue<Point> q=new LinkedList<>();
        q.offer(new Point(x,y));
        visited[x][y]=1;
        
        while(!q.isEmpty()){
            Point p=q.poll();
            for(int i = 0;i<4;i++){
                int nx=dx[i]+p.x;
                int ny=dy[i]+p.y;
                if(nx>=0 && nx<n && ny>=0 && ny<m && visited[nx][ny]==0 && maps[nx][ny]==1){
                    q.offer(new Point(nx,ny));
                    visited[nx][ny]=visited[p.x][p.y]+1;
                }
            }
        }
    }
    
    public int solution(int[][] maps) {
        int answer = 0;
        
        n=maps.length;
        m=maps[0].length;
        visited=new int[n][m];
        bfs(0,0,maps);
        if(visited[n-1][m-1]==0){
            return -1;
        }
        else{
            return visited[n-1][m-1];
        }
    }
}