//package ctp;

import java.util.*;
import java.io.*;



public class Main {
	
	
	
    public static void main(String[] args) throws Exception{
    	
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	int n=Integer.parseInt(br.readLine());
    
    	for(int i = 0;i<n;i++) {
    		int m=Integer.parseInt(br.readLine());
    		Map<String,List<String>> map=new HashMap<>();
    		int count=0;
    		int multVal=1;
    		for(int j = 0;j<m;j++) {
    			String line=br.readLine();
    			String[] arr=line.split(" ");
    			map.putIfAbsent(arr[1], new ArrayList<>());
    			map.get(arr[1]).add(arr[0]);
    		}
    		for(String key:map.keySet()) {
    			multVal*=(map.get(key).size()+1);
    		}
    		count=multVal-1;
    		bw.write(count+"\n");
    	}
    	
    	br.close();
    	bw.flush();
    	bw.close();
    }	
}
