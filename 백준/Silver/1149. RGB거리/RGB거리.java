//package ctp;

import java.util.*;



public class Main {
    
	final static int Red=0;
	final static int Green=1;
	final static int Blue=2;
    
    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int[][] cost=new int[n+1][3]; // 그 값들만 저장할배열
        int[][] dp=new int[n+1][3]; // 누적합을 저장할 배열
        
        for(int i = 1;i<=n;i++) {
        	for(int j=0;j<3;j++) {
        		cost[i][j]=sc.nextInt();
        	}
        }
        
        // 1번 행 저장할 배열
        dp[1][Red]=cost[1][Red];
        dp[1][Green]=cost[1][Green];
        dp[1][Blue]=cost[1][Blue];
        
        for(int i = 2;i<=n;i++) {
        	dp[i][Red]=cost[i][Red]+Math.min(dp[i-1][Green], dp[i-1][Blue]);
        	dp[i][Green]=cost[i][Green]+Math.min(dp[i-1][Red], dp[i-1][Blue]);
        	dp[i][Blue]=cost[i][Blue]+Math.min(dp[i-1][Green], dp[i-1][Red]);
        }
        
        System.out.println(Math.min(dp[n][Red],Math.min(dp[n][Green],dp[n][Blue])));
        
    }
}
