//package ctp;

import java.io.*;
import java.util.*;


public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		
		int[][] dp=new int[41][2];
		dp[0][0]=dp[1][1]=1;
		dp[0][1]=dp[1][0]=0;
		
		for(int i = 2;i<41;i++) {
			dp[i][0]=dp[i-1][0]+dp[i-2][0];
			dp[i][1]=dp[i-1][1]+dp[i-2][1];
		}
		
		int t=Integer.parseInt(br.readLine());
		for(int i = 0;i<t;i++) {
			int a=Integer.parseInt(br.readLine());
			bw.write(dp[a][0]+" "+dp[a][1]+"\n");
		}
		
		br.close();
		bw.flush();
		bw.close();
	}
}
