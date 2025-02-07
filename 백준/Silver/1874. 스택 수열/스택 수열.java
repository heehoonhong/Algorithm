//package ctp;

import java.util.*;

public class Main {
    public void solution(int[] arr) {
        Stack<Integer> stack = new Stack<>();
        StringBuilder sb = new StringBuilder(); // 🔥 출력 최적화
        int num = 1; // 현재 넣을 숫자

        for (int i = 0; i < arr.length; i++) {
            if (num <= arr[i]) {
                // 스택에 숫자 넣기 (1부터 arr[i]까지 push)
                while (num <= arr[i]) {
                    stack.push(num);
                    sb.append("+\n"); // 🔥 출력 버퍼에 추가
                    num++;
                }
            }
            // 스택에서 pop하여 arr[i]와 비교
            if (!stack.isEmpty() && stack.peek() == arr[i]) {
                stack.pop();
                sb.append("-\n"); // 🔥 출력 버퍼에 추가
            } else {
                System.out.println("NO"); // 올바른 수열을 만들 수 없는 경우
                return;
            }
        }
        
        System.out.println(sb.toString()); // 🔥 최종 출력 (출력 초과 방지)
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        T.solution(arr);
    }
}
