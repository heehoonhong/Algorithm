//package ctp;

import java.util.*;
import java.io.*;



public class Main {
	
	
	
    public static void main(String[] args) throws Exception{
    	Scanner sc=new Scanner(System.in);
    	String line=sc.nextLine();
    	Set<String> set=new HashSet<>();
    	
    	for(int i = 0;i<line.length();i++) {
    		for(int j =i+1;j<line.length()+1;j++) {
    			set.add(line.substring(i, j));
    		}
    	}
    	System.out.println(set.size());
    }	
}
