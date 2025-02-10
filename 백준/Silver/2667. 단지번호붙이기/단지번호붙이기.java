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
    
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int[][] visited, apartment;
    static int n;

    public void BFS(int x, int y, List<Integer> houses) {
        Queue<Point> queue = new LinkedList<>();
        queue.offer(new Point(x, y));
        visited[x][y] = 1;
        int count = 1; // 해당 단지 내 집의 개수

        while (!queue.isEmpty()) {
            Point temp = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = temp.x + dx[i];
                int ny = temp.y + dy[i];

                if (nx >= 1 && nx <= n && ny >= 1 && ny <= n && visited[nx][ny] == 0 && apartment[nx][ny] == 1) {
                    queue.offer(new Point(nx, ny));
                    visited[nx][ny] = 1;
                    count++; // 여기서 증가해야 정확함
                }
            }
        }
        houses.add(count);
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt(); // 기존의 전역 변수 n을 사용

        visited = new int[n + 1][n + 1];
        apartment = new int[n + 1][n + 1];

        for (int i = 1; i <= n; i++) {
            String line = sc.next();
            for (int j = 1; j <= n; j++) {
                apartment[i][j] = line.charAt(j - 1) - '0';
            }
        }

        List<Integer> houses = new ArrayList<>();
        int numApt = 0;

        // BFS 실행
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (apartment[i][j] == 1 && visited[i][j] == 0) {
                    T.BFS(i, j, houses);
                    numApt++;
                }
            }
        }

        // 결과 출력
        System.out.println(numApt);
        Collections.sort(houses);
        for (int house : houses) {
            System.out.println(house);
        }
    }
}
