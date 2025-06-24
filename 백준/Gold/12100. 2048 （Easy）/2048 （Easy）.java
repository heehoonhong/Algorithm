//package ctp;

import java.io.*;
import java.util.*;



public class Main {
	
	static int n,answer=0;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		n=Integer.parseInt(br.readLine());
		int[][] board=new int[n][n];
		for(int i = 0;i<n;i++) {
			StringTokenizer st=new StringTokenizer(br.readLine());
			for(int j = 0;j<n;j++) {
				board[i][j]=Integer.parseInt(st.nextToken());
			}
		}
		
		dfs(0,board);
		bw.write(answer+"\n");
		br.close();
		bw.flush();
		bw.close();
	
	}
	
	public static void dfs(int depth,int[][] arr) {
		if(depth==5) {
			for(int i = 0;i<n;i++) {
				for(int j = 0;j<n;j++) {
					answer=Math.max(answer, arr[i][j]);
				}
			}
			
			return;
		}
		
		dfs(depth+1,moveLeft(copyBoard(arr))); // 왼쪽으로 움직이기
		dfs(depth+1,moveRight(copyBoard(arr))); // 오른쪽으로 움직이기
		dfs(depth+1,moveUp(copyBoard(arr))); // 위로 움직이기
		dfs(depth+1,moveDown(copyBoard(arr))); // 아래로 움직이기 
	}
	
	static int[][] copyBoard(int[][] arr){
		int[][] copy=new int[n][n];
		for(int i = 0;i<n;i++) {
			for(int j = 0;j<n;j++) {
				copy[i][j]=arr[i][j];
			}
		}
		return copy;
	}
	
	static int[][] moveLeft(int[][] arr){
		for(int i = 0;i<n;i++) {
			
			List<Integer> list=new ArrayList<>();
			for(int j = 0;j<n;j++) {
				if(arr[i][j]!=0) {
					list.add(arr[i][j]);
				}
			}
			
			List<Integer> merged=new ArrayList<>();
			for(int k=0;k<list.size();k++) {
				if(k+1<list.size()&&list.get(k).equals(list.get(k+1))) {
					merged.add(list.get(k)*2);
					k++;
				}
				else {
					merged.add(list.get(k));
				}
			}
			
			
			for(int j = 0;j<merged.size();j++) {
				arr[i][j]=merged.get(j);
			}
			for(int j=merged.size();j<n;j++) {
				arr[i][j]=0;
			}
		}
		
		return arr;
	}
	
	static int[][] moveRight(int[][] arr){
		for(int i = 0;i<n;i++) {
			List<Integer> list=new ArrayList<>();
			for(int j=n-1;j>=0;j--) {
				if(arr[i][j]!=0) {
					list.add(arr[i][j]);
				}
			}
			
			List<Integer> merged = new ArrayList<>();
			for(int k=0;k<list.size();k++) {
				if(k+1<list.size()&&list.get(k).equals(list.get(k+1))) {
					merged.add(list.get(k)*2);
					k++;
				}
				else {
					merged.add(list.get(k));
				}
			}
			
			for(int j = 0;j<merged.size();j++) {
				arr[i][n-1-j]=merged.get(j);
			}
			for(int j=merged.size();j<n;j++) {
				arr[i][n-1-j]=0;
			}
		}
		return arr;
	}
	
	static int[][] moveUp(int[][] arr){
		for(int j=0;j<n;j++) {
			List<Integer> list=new ArrayList<>();
			for(int i = 0;i<n;i++) {
				if(arr[i][j]!=0) {
					list.add(arr[i][j]);
				}
			}
			
			List<Integer> merged=new ArrayList<>();
			for(int k = 0;k<list.size();k++) {
				if(k+1<list.size()&&list.get(k).equals(list.get(k+1))) {
					merged.add(list.get(k)*2);
					k++;
				}
				else {
					merged.add(list.get(k));
				}
			}
			
			for(int i=0;i<merged.size();i++) {
				arr[i][j]=merged.get(i);
			}
			for(int i=merged.size();i<n;i++) {
				arr[i][j]=0;
			}
			
		}
		
		return arr;
	}
	
	static int[][] moveDown(int[][] arr){
		for(int j=0;j<n;j++) {
			List<Integer> list=new ArrayList<>();
			for(int i = n-1 ;i>=0;i--) {
				if(arr[i][j]!=0) {
					list.add(arr[i][j]);
				}
			}
			
			List<Integer> merged=new ArrayList<>();
			for(int k = 0;k<list.size();k++) {
				if(k+1<list.size()&&list.get(k).equals(list.get(k+1))) {
					merged.add(list.get(k)*2);
					k++;
				}
				else {
					merged.add(list.get(k));
				}
			}
			
			for(int i=0;i<merged.size();i++) {
				arr[n-1-i][j]=merged.get(i);
			}
			for(int i=merged.size();i<n;i++) {
				arr[n-1-i][j]=0;
			}
			
		}
		return arr;
	}
}
