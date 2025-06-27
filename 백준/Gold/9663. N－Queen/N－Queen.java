import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N, ans = 0;
    static boolean[] col;     // 열 체크
    static boolean[] diag1;   // 주대각선 (row+col)
    static boolean[] diag2;   // 부대각선 (row-col+N)

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine().trim());

        col   = new boolean[N];
        diag1 = new boolean[2 * N];  // 인덱스 범위: 0 .. 2N-2
        diag2 = new boolean[2 * N];  // 인덱스 범위: 0 .. 2N-2

        dfs(0);
        System.out.println(ans);
    }

    // row: 현재 배치할 행 번호
    static void dfs(int row) {
        if (row == N) {
            ans++;
            return;
        }
        for (int j = 0; j < N; j++) {
            int d1 = row + j;
            int d2 = row - j + N;  // 음수 방지 위해 +N
            if (!col[j] && !diag1[d1] && !diag2[d2]) {
                col[j] = diag1[d1] = diag2[d2] = true;
                dfs(row + 1);
                col[j] = diag1[d1] = diag2[d2] = false;
            }
        }
    }
}
