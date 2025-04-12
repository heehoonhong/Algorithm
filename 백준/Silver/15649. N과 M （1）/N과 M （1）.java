

import java.io.*;
import java.util.*;


public class Main {
	
	static int[] arr;
	static int[] visited;
	static BufferedWriter bw;
	
	public static void dfs(int n,int m,int depth) throws IOException {
		if(depth==m) { // 종료조건: 깊이가 m이라면(수열의 길이가 m이라면 종료)
			for(int element:arr) {
				bw.write(element+" ");
			}
			bw.write("\n");
			return;
		}
		
		for(int i = 0;i<n;i++) {
			// n까지 순차적으로 돌면서
			// 방문하지 않았다면 방문처리를 하고,
			// 깊이를 증가시키고,
			// dfs
			// 다른 깊이의 visited를 하기 위해 방문 x 처리
			if(visited[i]==0) {
				visited[i]=1; // 방문 처리
				arr[depth]=i+1;
				dfs(n,m,depth+1);
				visited[i]=0;
			}
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		bw=new BufferedWriter(new OutputStreamWriter(System.out));
		
		String line=br.readLine();
		StringTokenizer st=new StringTokenizer(line);
		
		int n=Integer.parseInt(st.nextToken());
		int m=Integer.parseInt(st.nextToken());
		
		arr=new int[m];
		visited=new int[n];
		dfs(n,m,0);
		
		
		br.close();
		bw.flush();
		bw.close();
	}
}
