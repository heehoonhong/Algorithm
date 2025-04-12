

import java.io.*;
import java.util.*;


public class Main {
	
	static int[] arr;
	static int[] visited;
	static BufferedWriter bw;
	
	public static void dfs(int n,int m,int depth) throws IOException {
		
		if(depth==m) {
			for(int element:arr) {
				bw.write(element+" ");
			}
			bw.write("\n");
			return;
		}
		
		for(int i = 1;i<=n;i++) {
			arr[depth]=i;
			dfs(n,m,depth+1);
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
		visited=new int[n+1];
		dfs(n,m,0);
		
		
		br.close();
		bw.flush();
		bw.close();
	}
}
