//package ctp;

import java.util.*;

class Point {
    public int x, y;
    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    
    static int count=0;
    static int[][] visited;
    static int[][] farm;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int m, n;
    static Queue<Point> queue = new LinkedList<>();
    
    public void BFS() {
        while (!queue.isEmpty()) {
            Point temp = queue.poll();
            visited[temp.x][temp.y] = 1; // 방문 처리
            for (int i = 0; i < 4; i++) {
                int nx = temp.x + dx[i];
                int ny = temp.y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && visited[nx][ny] == 0 && farm[nx][ny] == 0) {
                    visited[nx][ny] = 1;
                    queue.offer(new Point(nx, ny));
                    farm[nx][ny] = farm[temp.x][temp.y] + 1; // ✅ 익은 날짜 증가
                }
            }
        }
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        m = sc.nextInt();
        n = sc.nextInt();
        farm = new int[n][m];
        visited = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                farm[i][j] = sc.nextInt();
                if (farm[i][j] == 1) {
                    queue.offer(new Point(i, j));
                }
            }
        }

        T.BFS();
        boolean flag = true;
        int answer = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (farm[i][j] == 0) flag = false; // ✅ 익지 않은 토마토가 있으면 실패
            }
        }
        if (flag) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    answer = Math.max(answer, farm[i][j]);
                }
            }
            System.out.println(answer - 1); // ✅ 날짜 계산을 위해 -1
        } else {
            System.out.println(-1);
        }
    }
}
