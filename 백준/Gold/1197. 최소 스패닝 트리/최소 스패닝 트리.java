import java.io.*;
import java.util.*;

// 1. 간선 정보를 담을 클래스 정의 (가중치 기준 정렬을 위해 Comparable 구현)
class Edge implements Comparable<Edge> {
    int u, v, weight;

    public Edge(int u, int v, int weight) {
        this.u = u;
        this.v = v;
        this.weight = weight;
    }

    // 정렬 기준 설정 (가중치 오름차순)
    @Override
    public int compareTo(Edge o) {
        return this.weight - o.weight;
    }
}

public class Main {
    static int[] parent; // 부모 노드 배열

    public static void main(String[] args) throws IOException {
        // 2. 빠른 입출력을 위한 BufferedReader 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        parent = new int[n + 1];
        // 부모 테이블 초기화 (자기 자신을 부모로 설정)
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        List<Edge> edges = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            edges.add(new Edge(a, b, c));
        }

        // 3. 간선 정렬 (파이썬의 sort key=lambda x:x[2] 와 동일)
        Collections.sort(edges);

        int total = 0;
        int cnt = 0;

        // 4. 크루스칼 알고리즘 수행
        // 파이썬 코드의 'while'문은 index 초과 에러 위험이 있어 안전한 for-each문으로 변경했습니다.
        for (Edge edge : edges) {
            // 이미 MST가 완성되었다면 조기 종료 (선택 사항)
            if (cnt == n - 1) break;

            if (find(edge.u) != find(edge.v)) {
                union(edge.u, edge.v);
                total += edge.weight;
                cnt++;
            }
        }

        System.out.println(total);
    }

    // 5. Find 함수 (경로 압축)
    static int find(int x) {
        if (x == parent[x]) {
            return x;
        }
        return parent[x] = find(parent[x]);
    }

    // 6. Union 함수
    static void union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);

        if (rootA != rootB) {
            // 작은 쪽으로 합치기 (작성하신 로직 반영)
            if (rootA < rootB) {
                parent[rootB] = rootA;
            } else {
                parent[rootA] = rootB;
            }
        }
    }
}