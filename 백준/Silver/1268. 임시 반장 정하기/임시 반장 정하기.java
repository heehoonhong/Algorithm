import java.util.*;

public class Main {

    public int solution(int n, int[][] arr) {
        int answer = 0;
        int[] count = new int[n];

        for (int i = 0; i < n; i++) { // 기준 학생 i
            for (int j = 0; j < n; j++) { // 비교할 학생 j
                for (int k = 0; k < 5; k++) { // 학년 (5년간)
                    if (i != j && arr[i][k] == arr[j][k]) { // i와 j가 같으면 비교 안 함
                        count[i]++;
                        break; // 같은 반인 걸 확인하면 break
                    }
                }
            }
        }

        int max = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            if (count[i] > max) {
                max = count[i];
                answer = i + 1; // 학생 번호는 1부터 시작
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[][] arr = new int[n][5]; // 5학년 동안의 반 정보

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 5; j++) {
                arr[i][j] = kb.nextInt();
            }
        }
        System.out.println(T.solution(n, arr));
        kb.close();
    }
}
