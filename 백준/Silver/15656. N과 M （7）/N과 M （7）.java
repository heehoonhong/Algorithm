

import java.io.*;
import java.util.*;


public class Main {
	
	static int[] arr;
	static int[] arr2;
	static BufferedWriter bw;
	static int[] visited;
	
	public static void dfs(int n,int m,int depth) throws IOException {
		if(depth==m) {
			for(int element:arr2) {
				bw.write(element+" ");
			}
			bw.write("\n");
			return;
		}
		
		for(int i = 0;i<n;i++) {
			arr2[depth]=arr[i];
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
		
		arr=new int[n];
		
		// 순차 출력을 위한 배열
		arr2=new int[m]; 
		
		visited=new int[n];
		
		String l=br.readLine();
		st=new StringTokenizer(l);
		for(int i = 0;i<n;i++) {
			arr[i]=Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr);
		
		dfs(n,m,0);
		
		br.close();
		bw.flush();
		bw.close();
	}
}
