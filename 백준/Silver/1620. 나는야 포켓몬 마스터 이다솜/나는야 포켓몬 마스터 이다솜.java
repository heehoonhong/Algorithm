//package ctp;

import java.util.*;
import java.io.*;



public class Main {
	
	
	
    public static void main(String[] args) throws Exception{
    	Scanner sc=new Scanner(System.in);
    	int n=sc.nextInt();
    	int m=sc.nextInt();
    	sc.nextLine();
    	Map<String,Integer> dogam=new HashMap<>();
    	Map<Integer,String> reversedDogam=new HashMap<>();
    	List<Object> answers=new ArrayList<>();
    	
    	for(int i = 0;i<n;i++) {
    		String line=sc.nextLine();
    		dogam.put(line, i+1);
    		reversedDogam.put(i+1, line);
    	}
    	
    	for(int i = 0;i<m;i++) {
    		String line=sc.nextLine();
    		if(Character.isAlphabetic(line.charAt(0))) {
    			answers.add(dogam.get(line));
    		}
    		else {
    			answers.add(reversedDogam.get(Integer.parseInt(line)));
    		}
    	}
    	
    	for(int i = 0;i<answers.size();i++) {
    		System.out.println(answers.get(i));
    	}
    	
    }	
}
