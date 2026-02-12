class Solution {
    public static int cnt=0;
    public static void dfs(int depth,int total,int[] numbers,int target){
        if(depth==numbers.length){
            if(total==target){
                cnt++;
            }
            return;
        }
        
        dfs(depth+1,total+numbers[depth],numbers,target);
        dfs(depth+1,total-numbers[depth],numbers,target);
    }
    
    public int solution(int[] numbers, int target) {
        dfs(0,0,numbers,target);
        return cnt;
    }
}