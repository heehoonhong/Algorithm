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
		int[] dp2=new int[n+1];
		
		String line=br.readLine();
		StringTokenizer st=new StringTokenizer(line);
		
		for(int i=1;i<=n;i++) {
			arr[i]=Integer.parseInt(st.nextToken());
		}
		
		
		for(int i = 1;i<=n;i++) {
			int max=0;
			for(int j=0;j<i;j++) {
				if(arr[j]<arr[i]) {
					max=Math.max(max, dp[j]);
				}
			}
			dp[i]=max+1;
		}
		
		
		
		for(int i=n;i>=1;i--) {
			int max=0;
			for(int j=n;j>i;j--) {
				if(arr[j]<arr[i]) {
					max=Math.max(max, dp2[j]);
				}
			}
			dp2[i]=max+1;
			
		}
		for(int i = 1;i<=n;i++) {
			dp2[i]--;
		}
		
		
		for(int i = 1;i<=n;i++) {
			dp[i]+=dp2[i];
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
