//package ctp;

import java.io.*;
import java.util.*;


public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n=Integer.parseInt(br.readLine());
		
		int[] T=new int[n+1];
		int[] P=new int[n+1];
		int[] dp=new int[n+2];
		
		for(int i = 1;i<=n;i++) {
			String line=br.readLine();
			StringTokenizer st=new StringTokenizer(line);
			T[i]=Integer.parseInt(st.nextToken());
			P[i]=Integer.parseInt(st.nextToken());
		}
		
		for(int i=n;i>=1;i--) {
			if(i+T[i]-1<=n) {
				dp[i]=Math.max(dp[i+1], dp[T[i]+i]+P[i]);
			}
			else {
				dp[i]=dp[i+1];
			}
		}
		
		bw.write(dp[1]+"\n");
		
		br.close();
		bw.flush();
		bw.close();
	}
}
