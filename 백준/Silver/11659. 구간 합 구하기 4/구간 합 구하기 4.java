//package ctp;

import java.io.*;
import java.util.*;



public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		
		String line=br.readLine();
		StringTokenizer st=new StringTokenizer(line);
		
		int n=Integer.parseInt(st.nextToken());
		int m=Integer.parseInt(st.nextToken());
		
		int[] arr=new int[n];
		int[] S=new int[n+1];
		
		String l=br.readLine();
		st=new StringTokenizer(l);
		for(int i = 0;i<arr.length;i++) {
			arr[i]=Integer.parseInt(st.nextToken());
			if(i==0) {
				S[i+1]=arr[i];
			}
			else {
				S[i+1]+=S[i]+arr[i];
			}
			//bw.write(S[i]+" ");
		}
		//bw.write(S[S.length-1]+" ");
		
		
		for(int i=0;i<m;i++) {
			String ll=br.readLine();
			st=new StringTokenizer(ll);
			int prev,last;
			prev=Integer.parseInt(st.nextToken());
			last=Integer.parseInt(st.nextToken());
			bw.write(S[last]-S[prev-1]+"\n");
			
		}
		
		
		
		br.close();
		bw.flush();
		bw.close();
	}
}
