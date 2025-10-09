class Solution {
    public static int[][] arr1Map;
    public static int[][] arr2Map;
    
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = {};
        answer=new String[n];
        for(int i = 0;i<n;i++){
            answer[i]="";
        }
        
        arr1Map=new int[n][n];
        arr2Map=new int[n][n];
        
        for(int i=0;i<n;i++){
            for(int j=n-1;j>=1;j--){
                arr1Map[i][j]=arr1[i]%2;
                arr1[i]=arr1[i]/2;
                arr2Map[i][j]=arr2[i]%2;
                arr2[i]=arr2[i]/2;
            }
            // 맨 마지막
            arr1Map[i][0]=arr1[i];
            arr2Map[i][0]=arr2[i];
        }
        
        for(int i = 0;i<n;i++){
            for(int j = 0;j<n;j++){
                if(arr1Map[i][j]==1 || arr2Map[i][j]==1){
                    answer[i]+="#";
                }
                else if(arr1Map[i][j]==0 && arr2Map[i][j]==0){
                    answer[i]+=" ";
                }
            }
        }
        
        return answer;
    }
}