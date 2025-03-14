//package ctp;

import java.util.*;
import java.io.*;



public class Main {
	
	
	
    public static void main(String[] args) throws Exception{
    
    	Scanner sc=new Scanner(System.in);
    	int n=sc.nextInt();
    	sc.nextLine();
    	Map<String,String> map=new HashMap<>();
    	
    	for(int i = 0;i<n;i++) {
    		String line=sc.nextLine();
    		String[] arr=line.split(" ");
    		if(arr[1].equals("enter")) {
    			map.put(arr[0],arr[1]);
    		}
    		if(arr[1].equals("leave")) {
    			map.remove(arr[0]);
    		}
    	}
    	
    	List<String> keys=new ArrayList<>(map.keySet());
    	
    	Collections.sort(keys,Collections.reverseOrder());
    	
    	
    	for(String key:keys) {
    		System.out.println(key);
    	}
    	
    }	
}
