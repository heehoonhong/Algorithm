//package ctp;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        if (n == 0) { // 예외처리: 계단이 없는 경우
            System.out.println(0);
            return;
        }

        int[] stairs = new int[n + 1];
        int[] maxScores = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            stairs[i] = sc.nextInt();
        }

        maxScores[1] = stairs[1];

        if (n >= 2) {
            maxScores[2] = stairs[1] + stairs[2];
        }
        
        if (n >= 3) {
            maxScores[3] = stairs[3] + Math.max(stairs[1], stairs[2]);
        }

        for (int i = 4; i <= n; i++) {
            maxScores[i] = Math.max(maxScores[i - 2], stairs[i - 1] + maxScores[i - 3]) + stairs[i];
        }

        System.out.println(maxScores[n]);
    }
}
