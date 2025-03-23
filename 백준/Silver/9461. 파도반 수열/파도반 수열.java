//package ctp;

import java.io.*;
import java.util.*;


public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		
		long[] dp=new long[101];
		dp[1]=1;
		dp[2]=1;
		dp[3]=1;
		
		for(int i=4;i<=100;i++) {
			dp[i]=dp[i-2]+dp[i-3];
		}
		
		int t=Integer.parseInt(br.readLine());
		for(int i = 0;i<t;i++) {
			int num=Integer.parseInt(br.readLine());
			bw.write(dp[num]+"\n");
			
		}
		
		
		br.close();
		bw.flush();
		bw.close();
	}
}
