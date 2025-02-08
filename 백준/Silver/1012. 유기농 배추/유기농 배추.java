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
    
    static int[][] visited;
    static int[][] farm;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int m, n;

    public void BFS(int x, int y) {
        Queue<Point> queue = new LinkedList<>();
        queue.offer(new Point(x, y));
        visited[x][y] = 1;

        while (!queue.isEmpty()) {
            Point temp = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = temp.x + dx[i];
                int ny = temp.y + dy[i];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m && visited[nx][ny] == 0 && farm[nx][ny] == 1) {
                    visited[nx][ny] = 1;
                    queue.offer(new Point(nx, ny));
                }
            }
        }
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int numTestCases = sc.nextInt();
        List<Integer> results = new ArrayList<>(); // 🔥 출력값을 저장하는 리스트

        for (int ebe = 0; ebe < numTestCases; ebe++) {
            m = sc.nextInt(); // 가로 길이
            n = sc.nextInt(); // 세로 길이
            int k = sc.nextInt(); // 배추 개수

            visited = new int[n][m];
            farm = new int[n][m];

            for (int j = 0; j < k; j++) {
                int a = sc.nextInt();
                int b = sc.nextInt();
                farm[b][a] = 1;
            }

            int count = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (farm[i][j] == 1 && visited[i][j] == 0) {
                        T.BFS(i, j);
                        count++;
                    }
                }
            }
            results.add(count); // 🔥 결과를 리스트에 저장
        }
        
        sc.close(); // 🔥 모든 입력이 끝난 후 Scanner 닫기
        
        // 🔥 모든 입력을 받은 후 한 번에 출력
        for (int i = 0; i < results.size(); i++) {
            System.out.println(results.get(i));
        }
    }
}
