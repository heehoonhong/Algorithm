//package ctp;

import java.util.*;
import java.io.*;



public class Main {
		
    public static void main(String[] args) throws Exception{
        Scanner sc=new Scanner(System.in);
        
        int[] a=new int[3];
        for(int i = 0;i<3;i++) {
        	a[i]=sc.nextInt();
        }
        int cnt=0;
        if(a[0]==a[1]) cnt++;
        if(a[1]==a[2]) cnt++;
        if(a[0]==a[2]) cnt++;
        
        if(cnt==3) {
        	System.out.println(10000+a[0]*1000);
        }
        else if(cnt==1) {
        	if(a[0]==a[1]) {
        		System.out.println(1000+a[0]*100);
        	}
        	else if(a[1]==a[2]) {
        		System.out.println(1000+a[1]*100);
        	}
        	else if(a[2]==a[0]) {
        		System.out.println(1000+a[2]*100);
        	}
        }
        else {
        	int max=0;
        	for(int i = 0;i<3;i++) {
        		if(max<=a[i]) {
        			max=a[i];
        		}
        	}
        	System.out.println(max*100);
        }
    }

	
}
