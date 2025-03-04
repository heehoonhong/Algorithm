//package ctp;

import java.util.*;

public class Main {
    static int[] fib;

    public static int fibo(int n) {
        if (fib[n] != -1) { // 이미 계산된 값이면 반환
            return fib[n];
        }
        if (n == 1 || n == 2) { // 기본값 설정 (F(1) = 1, F(2) = 2)
            return fib[n] = n;
        }

        // 재귀 호출 + 모듈러 연산 적용
        return fib[n] = (fibo(n - 1) + fibo(n - 2)) % 15746;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();

        fib = new int[n + 1];
        Arrays.fill(fib, -1); // 초기값 -1로 설정하여 메모이제이션 여부 확인 가능

        System.out.println(fibo(n));
    }
}
