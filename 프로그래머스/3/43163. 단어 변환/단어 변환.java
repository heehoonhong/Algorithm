class Solution {
    
    public static int answer;
    public static int[] visited;
    
    public int solution(String begin, String target, String[] words) {
        answer = 51;
        visited=new int[words.length];
        
        dfs(begin,target,words,0);
        
        if(answer==51){
            answer=0;
        }
        
        return answer;
    }
    
    public static void dfs(String begin,String target,String[] words,int depth){
        if(begin.equals(target)){
            //answer=Math.min(depth,answer);
            answer=Math.min(answer,depth);
            return;
        }
        
        for(int i=0;i<words.length;i++){
            if(canChange(begin,words[i])&&visited[i]==0){
                visited[i]=1;
                dfs(words[i],target,words,depth+1);
                visited[i]=0;
            }
        }
    }
    
    public static boolean canChange(String begin, String newWord){
        
        int eqCount=0;
        
        for(int i=0;i<begin.length();i++){
            if(begin.charAt(i)!=newWord.charAt(i)){
                eqCount++;
            }
        }
        
        if(eqCount==1){
            return true;
        }
        else{
            return false;
        }
            
    }
}