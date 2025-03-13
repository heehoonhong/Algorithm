//package ctp;

import java.util.*;
import java.io.*;



public class Main {
	
	
	
    public static void main(String[] args) throws Exception{
    
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
	
    	StringTokenizer st=new StringTokenizer(br.readLine());
    	int n=Integer.parseInt(st.nextToken());
    	
    	int[] nArr=new int[n];
    	st=new StringTokenizer(br.readLine());
    	for(int i = 0;i<n;i++) {
    		nArr[i]=Integer.parseInt(st.nextToken());
    	}
    	
    	st=new StringTokenizer(br.readLine());
    	int m=Integer.parseInt(st.nextToken());
    	
    	st=new StringTokenizer(br.readLine());
    	int[] mArr=new int[m];
    	for(int i = 0;i<m;i++) {
    		mArr[i]=Integer.parseInt(st.nextToken());
    	}
    	
    	Map<Integer,Integer> countMap=new HashMap<>();
    	for(int i = 0;i<n;i++) {
    		countMap.put(nArr[i], countMap.getOrDefault(nArr[i], 0)+1);
    	}
    	
    	for(int i = 0;i<m;i++) {
    		bw.write(countMap.getOrDefault(mArr[i], 0)+" ");
    	}
    	
    	
    	bw.newLine();
        bw.flush();
        bw.close();
        br.close();

    	
    	
    	
    
    }
	
	
        	
}
