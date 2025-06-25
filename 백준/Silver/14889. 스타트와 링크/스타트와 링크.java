//package ctp;

import java.io.*;
import java.util.*;



public class Main {
	
	
	static int[][] arr;
	static int n,m;
	static int answer=Integer.MAX_VALUE;
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		
		n=Integer.parseInt(br.readLine());
		m=n/2;
		arr=new int[n][n];
		for(int i = 0;i<n;i++) {
			StringTokenizer st=new StringTokenizer(br.readLine());
			for(int j=0;j<n;j++) {
				arr[i][j]=Integer.parseInt(st.nextToken());
			}
		}
		
		dfs(0,new ArrayList<>(),new ArrayList<>());
		bw.write(answer+"\n");
		
		br.close();
		bw.flush();
		bw.close();
	}
	
	public static void dfs(int k,List<Integer> teamA,List<Integer> teamB) {
		if(k==n) {
			if(teamA.size()==m&&teamB.size()==m) {
				int aTotal=0,bTotal=0;
				for(int i = 0;i<m;i++) {
					for(int j=0;j<m;j++) {
						aTotal+=arr[teamA.get(i)][teamA.get(j)];
						bTotal+=arr[teamB.get(i)][teamB.get(j)];
					}
				}
				answer=Math.min(answer, Math.abs(aTotal-bTotal));
			}
			return;
		}
		
		if(teamA.size()<m) {
			teamA.add(k);
			dfs(k+1,teamA,teamB);
			teamA.remove(teamA.size()-1);
		}
		
		if(teamB.size()<m) {
			teamB.add(k);
			dfs(k+1,teamA,teamB);
			teamB.remove(teamB.size()-1);
		}
	}
}
