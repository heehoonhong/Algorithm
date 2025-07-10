//package ctp;

import java.io.*;
import java.util.*;



public class Main {
	
	public static int num,maxCount;
	public static int[] visited;
	public static int[] arr;
	public static BufferedWriter bw;
	public static int[] selected;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		bw=new BufferedWriter(new OutputStreamWriter(System.out));
		
		String line=br.readLine();
		StringTokenizer st=new StringTokenizer(line);
		
		num=Integer.parseInt(st.nextToken());
		maxCount=Integer.parseInt(st.nextToken());
		visited=new int[num+1];
		arr=new int[num+1];
		selected=new int[maxCount];
		
		for(int i = 0;i<arr.length;i++) {
			arr[i]=i;
		}
		
		//visited[0]=1;
		dfs(0);
		
		br.close();
		bw.flush();
		bw.close();
	}
	
	public static void dfs(int currentCount) throws IOException {
		if(currentCount==maxCount) {
			for(int i = 0;i<maxCount;i++) {
				bw.write(selected[i]+" ");
			}
			bw.write("\n");
			return;
		}
		
		// 마지막이 아니라면 
		// for 문을 돌면서 방문하지 않은 노드들을  
		// 하나씩 방문 처리하면서 dfs
		for(int i = 1;i<visited.length;i++) {
			if(visited[i]==0) {
				visited[i]=1;
				//bw.write(arr[i]+" ");
				selected[currentCount]=arr[i];
				dfs(currentCount+1);
				visited[i]=0;
			}
		}
	}
}
