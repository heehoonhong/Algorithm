//package ctp;

import java.util.*;
import java.io.*;



public class Main {
	
	
	
    public static void main(String[] args) throws Exception{
    	
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	StringTokenizer st=new StringTokenizer(br.readLine());
    	int n=Integer.parseInt(st.nextToken());
    	int m=Integer.parseInt(st.nextToken());
    	Map<String,String> map=new HashMap<>();
    	
    	for(int i = 0;i<n;i++) {
    		String line=br.readLine();
    		String[] arr=line.split(" ");
    		map.put(arr[0], arr[1]);
    	}
    	for(int i = 0;i<m;i++) {
    		String line=br.readLine();
    		if(map.containsKey(line)) {
    			bw.write(map.get(line)+"\n");
    		}
    	}
    	bw.flush();
    	br.close();
    	bw.close();
    	
    }	
}
