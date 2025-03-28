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
		
		for(int i = 1;i<=n;i++) {
			arr[i]=Integer.parseInt(br.readLine());
		}
		
		if (n >= 1) dp[1] = arr[1];
        if (n >= 2) dp[2] = arr[1] + arr[2];
        if (n >= 3) dp[3] = Math.max(dp[2], Math.max(arr[1] + arr[3], arr[2] + arr[3]));

        for (int i = 4; i <= n; i++) {
            dp[i] = Math.max(dp[i - 1],
                        Math.max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i]));
        }
		
		bw.write(dp[n]+"\n");
		
		br.close();
		bw.flush();
		bw.close();
	}
}
