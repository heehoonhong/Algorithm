//package ctp;

import java.io.*;
import java.util.*;

public class Main {
	
	static final int INF=999999;
	
    public static void main(String[] args) throws Exception {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	String line=br.readLine();
    	StringTokenizer st=new StringTokenizer(line);
    	int n=Integer.parseInt(st.nextToken());
    	int m=Integer.parseInt(st.nextToken());
    	
    	int[][] graph=new int[n+1][n+1];
    	
    	// 초기 거리 설정
    	for(int i = 1;i<=n;i++) {
    		for(int j = 1;j<=n;j++) {
    			if(i==j) {
    				graph[i][j]=0;
    			}
    			else {
    				graph[i][j]=INF;
    			}
    		}
    	}
    	
    	for(int i = 0;i<m;i++) {
    		String l=br.readLine();
    		st=new StringTokenizer(l);
    		int a=Integer.parseInt(st.nextToken());
    		int b=Integer.parseInt(st.nextToken());
    		graph[a][b]=1;
    		graph[b][a]=1;
    	}
    	
    	for(int k = 1;k<=n;k++) {
    		for(int i = 1;i<=n;i++) {
    			for(int j = 1;j<=n;j++) {
    				graph[i][j]=Math.min(graph[i][j], graph[i][k]+graph[k][j]);
    			}
    		}
    	}
    	
    	int cmpSum=INF;
    	int personNum=0;
    	for(int i = 1;i<=n;i++) {
    		int sum=0;
    		for(int j = 1;j<=n;j++) {
    			sum+=graph[i][j];
    		}
    		
    		if(sum<cmpSum) {
    			cmpSum=sum;
    			personNum=i;
    		}
    	}
    	
    	bw.write(personNum+"\n");
    	
    	br.close();
    	bw.flush();
    	bw.close();
    }
}
