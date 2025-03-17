//package ctp;

import java.util.*;
import java.io.*;



public class Main {
	
	
	
    public static void main(String[] args) throws Exception{
    	
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	int n=Integer.parseInt(br.readLine());
    	Deque<Integer> deque=new LinkedList<>();
    	
    	for(int i = 0;i<n;i++) {
    		String line=br.readLine();
    		String[] arr=line.split(" ");
    		if(arr[0].equals("push_front")) {
    			deque.addFirst(Integer.parseInt(arr[1]));
    		}
    		else if(arr[0].equals("push_back")) {
    			deque.addLast(Integer.parseInt(arr[1]));
    		}
    		else if(arr[0].equals("pop_front")) {
    			if(deque.isEmpty()) {
    				bw.write(-1+"\n");
    			}
    			else {
    				bw.write(deque.removeFirst()+"\n");
    			}
    		}
    		else if(arr[0].equals("pop_back")) {
    			if(deque.isEmpty()) {
    				bw.write(-1+"\n");
    			}
    			else {
    				bw.write(deque.removeLast()+"\n");
    			}
    		}
    		else if(arr[0].equals("size")) {
    			bw.write(deque.size()+"\n");
    		}
    		else if(arr[0].equals("empty")) {
    			if(deque.isEmpty()) {
    				bw.write(1+"\n");
    			}
    			else {
    				bw.write(0+"\n");
    			}
    		}
    		else if(arr[0].equals("front")) {
    			if(deque.isEmpty()) {
    				bw.write(-1+"\n");
    			}
    			else {
    				bw.write(deque.peekFirst()+"\n");
    			}
    		}
    		else if(arr[0].equals("back")) {
    			if(deque.isEmpty()) {
    				bw.write(-1+"\n");
    			}
    			else {
    				bw.write(deque.peekLast()+"\n");
    			}
    		}
    		
    		
    	}
    	bw.flush();  
        bw.close();
        br.close();
    	
    	
    }	
}
