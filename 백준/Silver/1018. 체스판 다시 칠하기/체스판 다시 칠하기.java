//package ctp;

import java.util.*;
import java.io.*;



public class Main {
	
	public static int getSolution(int startRow,int startCol,String[] arr) {
		String[] chessCompare= {"WBWBWBWB","BWBWBWBW"};
		// i가 row 시작번호이고, j가 col 시작번호임
		// 그니까 i+8까지 돌고, j+8까지 돌면 됨.
		
		int whiteCount=0;
		int blackCount=0;
		
		for(int i = 0;i<8;i++) {
			int row=startRow+i;
			for(int j = 0;j<8;j++) {
				int col=startCol+j;
				if(i%2==0) {
					if(arr[row].charAt(col)!=chessCompare[0].charAt(j)) {
						whiteCount++;
					}
				}
				else {
					if(arr[row].charAt(col)!=chessCompare[1].charAt(j)) {
						whiteCount++;
					}
				}
			}
		}
		
		for(int i = 0;i<8;i++) {
			int row=startRow+i;
			for(int j=0;j<8;j++) {
				int col=startCol+j;
				if(i%2==0) {
					if(arr[row].charAt(col)!=chessCompare[1].charAt(j)) {
						blackCount++;
					}
				}
				else {
					if(arr[row].charAt(col)!=chessCompare[0].charAt(j)) {
						blackCount++;
					}
				}
			}
		}
		
		
		return Math.min(whiteCount, blackCount);
	}
	
    public static void main(String[] args) throws Exception{
        Scanner sc=new Scanner(System.in);
        int row=sc.nextInt();
        int col=sc.nextInt();
        sc.nextLine();
        
        String[] arr=new String[row];
        // 입력받기
    	for(int i = 0;i<row;i++) {
    		arr[i]=sc.nextLine();
    	}
    	
    	
    	int sol=Integer.MAX_VALUE;
    	
    	// 8 x 8 체스판 뽑기
    	for(int i = 0;i<=row-8;i++) {
    		for(int j = 0;j<=col-8;j++) {
    			int curSol=getSolution(i,j,arr);
    			if(curSol<sol) {
    				sol=curSol;
    			}
    		}
    	}
    	System.out.println(sol);
    	sc.close();
    	
	}
	
	
        	
}
