//package ctp;

import java.util.*;
import java.io.*;



public class Main {
	
	
	
    public static void main(String[] args) throws Exception{
    	Scanner sc=new Scanner(System.in);
    	int a=sc.nextInt();
    	int b=sc.nextInt();
    	
    	Set<Integer> setA=new HashSet<>();
    	Set<Integer> setB=new HashSet<>();
    	
    	for(int i = 0;i<a;i++) {
    		int num=sc.nextInt();
    		setA.add(num);
    	}
    	for(int i = 0;i<b;i++) {
    		int num=sc.nextInt();
    		setB.add(num);
    	}
    	
    	int answer=0;
    	for(int num:setA) {
    		if(!setB.contains(num)) {
    			answer++;
    		}
    	}
    	for(int num:setB) {
    		if(!setA.contains(num)) {
    			answer++;
    		}
    	}
    	
    	System.out.println(answer);
    }	
}
