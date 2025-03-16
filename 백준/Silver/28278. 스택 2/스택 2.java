//package ctp;

import java.util.*;
import java.io.*;



public class Main {
	
	
	
    public static void main(String[] args) throws Exception{
    	BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	int n=Integer.parseInt(br.readLine());
    	Stack<Integer> stack=new Stack<>();
    	
    	for(int i = 0;i<n;i++) {
    		String line=br.readLine();
    		String[] arr=line.split(" ");
    		if(arr[0].equals("1")) {
    			int num=Integer.parseInt(arr[1]);
    			stack.push(num);
    		}
    		else if(arr[0].equals("2")) {
    			if(stack.isEmpty()) {
    				//System.out.println(-1);
    				bw.write(-1+"\n");
    			}
    			else {
    				int num=stack.pop();
    				
    				bw.write(num+"\n");
    			}
    		}
    		else if(arr[0].equals("3")) {
    			bw.write(stack.size()+"\n");
    		}
    		else if(arr[0].equals("4")) {
    			if(stack.isEmpty()) {
    				bw.write(1+"\n");
    			}
    			else {
    				bw.write(0+"\n");
    			}
    		}
    		else if(arr[0].equals("5")) {
    			if(stack.isEmpty()) {
    				bw.write(-1+"\n");
    			}
    			else {
    				bw.write(stack.peek()+"\n");
    				
    			}
    		}
    	}
    	bw.flush();
    	bw.close();
    			
    }	
}
