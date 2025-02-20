//package ctp;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        // 정사각형 배열로 크기 설정
        int[][] cost = new int[n + 1][n + 1]; 
        int[][] dp = new int[n + 1][n + 1]; 

        // 비용 입력 받기
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) { // 삼각형 구조로 입력
                cost[i][j] = sc.nextInt();
            }
        }

        // 초기값 설정
        dp[1][1] = cost[1][1];

        // DP 진행 (누적 최대 합)
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                if (j == 1) {  // 맨 왼쪽 (한 칸 위에서만 내려올 수 있음)
                    dp[i][j] = cost[i][j] + dp[i - 1][j];
                } 
                else if (j == i) {  // 맨 오른쪽 (왼쪽 대각선에서만 올 수 있음)
                    dp[i][j] = cost[i][j] + dp[i - 1][j - 1];
                } 
                else {  // 중간 위치 (두 방향에서 올 수 있음)
                    dp[i][j] = cost[i][j] + Math.max(dp[i - 1][j - 1], dp[i - 1][j]);
                }
            }
        }

        // 마지막 행에서 최댓값 찾기
        int result = 0;
        for (int i = 1; i <= n; i++) {
            result = Math.max(result, dp[n][i]);
        }

        // 결과 출력
        System.out.println(result);
    }
}
