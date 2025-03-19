//package ctp;

import java.io.*;
import java.util.*;

public class Main {
	
	static int[][] graph;
	static int n;
	static final int INF=99999;
	
    public static void main(String[] args) throws Exception {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	String line=br.readLine();
    	StringTokenizer st=new StringTokenizer(line);
    	
    	n=Integer.parseInt(st.nextToken());
    
    	graph=new int[n+1][n+1];
    	
    	for(int i = 1;i<=n;i++) {
    		String l=br.readLine();
    		st=new StringTokenizer(l);
    		for(int j = 1;j<=n;j++) {
    			graph[i][j]=Integer.parseInt(st.nextToken());
    		}
    	}
    	
    	
    	// 플로이드-와샬 알고리즘 (경로 존재 여부 확인)
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (graph[i][k] == 1 && graph[k][j] == 1) {
                        graph[i][j] = 1;  // 경로가 존재하면 1로 갱신
                    }
                }
            }
        }

        // 결과 출력
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                bw.write(graph[i][j] + " ");
            }
            bw.write("\n");
        }
    	
    	br.close();
    	bw.flush();
    	bw.close();
    }
}
