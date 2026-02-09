//package ctp;

import java.io.*;
import java.util.*;

public class Main {
   
	public static class Node{
		int value;
		int index;
		public Node(int value,int index) {
			this.value=value;
			this.index=index;
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		int n=Integer.parseInt(br.readLine());
		StringTokenizer st=new StringTokenizer(br.readLine());
		Stack<Node> stack=new Stack<>();
		int[] arr=new int[n];
		int[] result=new int[n];
		for(int i = 0;i<n;i++) {
			result[i]=-1;
		}
		for(int i=0;i<n;i++) {
			arr[i]=Integer.parseInt(st.nextToken());
		}
		for(int i = 0;i<n-1;i++) {
			while(!stack.isEmpty() && stack.peek().value<arr[i]) {
				result[stack.peek().index]=arr[i];
				stack.pop();
			}
			stack.push(new Node(arr[i],i));
		}
		while(!stack.isEmpty()) {
			if(stack.peek().value<arr[n-1]) {
				result[stack.peek().index]=arr[n-1];
			}
			else {
				result[stack.peek().index]=-1;
			}
			stack.pop();
		}
		
		for(int i = 0;i<n;i++) {
			bw.write(result[i]+" ");
		}
		bw.write("\n");
		
		br.close();
		bw.flush();
		bw.close();
	}
	
	
}

