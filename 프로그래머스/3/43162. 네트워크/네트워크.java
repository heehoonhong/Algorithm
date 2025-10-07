class Solution {
    
    int answer;
    static int[] visited;
    public int solution(int n, int[][] computers) {
        visited=new int[n];
        answer = 0;
        
        for(int i = 0;i<n;i++){
            if(visited[i]==0){
                answer++;
                dfs(n,computers,i);
            }
        }
        
        return answer;
    }
    
    public void dfs(int n,int[][] computers,int index){
        visited[index]=1; // 방문 처리
        
        for(int i = 0;i<n;i++){
            if(visited[i]==0&&computers[index][i]==1){
                dfs(n,computers,i);
            }
        }
    }
}