//package ctp;

import java.io.*;
import java.util.*;


public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n=Integer.parseInt(br.readLine());
		
		int[] arr=new int[n+1];
		int[] dp=new int[n+1];
		
		String line=br.readLine();
		StringTokenizer st=new StringTokenizer(line);
		
		for(int i = 1;i<=n;i++) {
			arr[i]=Integer.parseInt(st.nextToken());
		}
		
		
		dp[0]=0;
		
		
		
		
		for(int i = 1;i<=n;i++) {
			int max=0;
			for(int j= 1;j<=i;j++) {
				if(arr[j]<arr[i]) {
					max=Math.max(max, dp[j]);
				}
			}
			dp[i]=max+1;
			//bw.write(dp[i]+"\n");
		}
		
		
		
		
		int mMax=0;
		for(int i = 1;i<=n;i++) {
			mMax=Math.max(mMax, dp[i]);
		}
		bw.write(mMax+"\n");
		
		br.close();
		bw.flush();
		bw.close();
	}
}
