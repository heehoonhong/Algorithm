import java.util.*;

class Solution {
    public static void dfs(int v){
            visited[v]=1;
            
            for(int nextNode:graph[v]){
                if(visited[nextNode]==0){
                    visited[nextNode]=1;
                    dfs(nextNode);
                }
            }
    }
    static ArrayList<Integer>[] graph;
    static int[] visited;
    public int solution(int n, int[][] computers) {
        int cnt=0;
        visited=new int[n];
        // [] -> 리스트  따라서 리스트에 대한 배열이니까 이렇게가 맞음
        // 왼쪽이 안쪽, 오른쪽이 바깥쪽 자료구조(형)
        graph=new ArrayList[n];
        for(int i = 0;i<n;i++){
            graph[i]=new ArrayList<Integer>();
        }
        for(int i = 0;i<n;i++){
            for(int j = 0;j<n;j++){
                if(i!=j && computers[i][j]==1){
                    graph[i].add(j);
                    graph[j].add(i);
                }
            }
        }
        
        
        
        for(int i=0;i<n;i++){
            if(visited[i]==0){
                dfs(i);
                cnt++;
            }
        }
        
        return cnt;
    }
}