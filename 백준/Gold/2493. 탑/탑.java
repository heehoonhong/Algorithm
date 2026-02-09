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
		
		for(int i=0;i<n;i++) {
			arr[i]=Integer.parseInt(st.nextToken());
		}
		for(int i=n-1;i>=0;i--) {
			while(!stack.isEmpty() && stack.peek().value<arr[i]) {
				result[stack.peek().index]=i+1;
				stack.pop();
			}
			stack.push(new Node(arr[i],i));
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

