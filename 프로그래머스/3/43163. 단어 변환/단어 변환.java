class Solution {
    public static int[] visited;
    public static int cnt;
    
    public static boolean check(String str1,String str2){
        int cc=0;
        for(int i = 0;i<str1.length();i++){
            if(str1.charAt(i)!=str2.charAt(i)){
                cc++;
            }
        }
        //System.out.println(cc);
        if(cc==1) return true;
        else return false;
    }
    
    public static void dfs(String currentWord,int currentCnt,String target,String[] words){
        if(currentCnt>cnt){
            return;
        }
        
        
        if(currentWord.equals(target)){
            //System.out.println("asdf");
            cnt=Math.min(cnt,currentCnt);
            return;
        }
        for(int i = 0;i<words.length;i++){
            boolean flag=check(currentWord,words[i]);
            //System.out.println(flag);
            if(flag && visited[i]==0){
                visited[i]=1;
                dfs(words[i],currentCnt+1,target,words);
                visited[i]=0;
            }
        }
    }
    
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        cnt=1000;
        visited=new int[words.length];
        dfs(begin,0,target,words);
        if(cnt==1000){
            return 0;
        }
        else{
            return cnt;
        }
    }
}