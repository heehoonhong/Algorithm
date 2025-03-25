//package ctp;

import java.io.*;
import java.util.*;


public class Main {
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n=Integer.parseInt(br.readLine());
		int[] arr=new int[n];
		
		String line=br.readLine();
		StringTokenizer st=new StringTokenizer(line);
		for(int i = 0;i<n;i++) {
			arr[i]=Integer.parseInt(st.nextToken());
		}
		
		int[] dp=new int[n];
		
		dp[0]=arr[0];
		
		int max1=Integer.MIN_VALUE;
		
		
		for(int i=1;i<n;i++) {
			dp[i]=Math.max(dp[i-1]+arr[i], arr[i]);
		}
		
		int max=Integer.MIN_VALUE;
		for(int i = 0;i<n;i++) {
			max=Math.max(max, dp[i]);
		}
		
		bw.write(max+"\n");
		
		br.close();
		bw.flush();
		bw.close();
	}
}
