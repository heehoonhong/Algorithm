//package ctp;

import java.io.*;
import java.util.*;


public class Main {
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n=Integer.parseInt(br.readLine());
		
		int[] dp=new int[1001];
		dp[1]=1%10007;
		dp[2]=3%10007;
		
		for(int i = 3;i<=1000;i++) {
			dp[i]=(dp[i-1]+2*dp[i-2])%10007;
		}
		
		
		
		
		bw.write(dp[n]+"\n");
		
		br.close();
		bw.flush();
		bw.close();
	}
}
