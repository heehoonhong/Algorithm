//package ctp;

import java.util.*;
import java.io.*;



public class Main {
		
    public static void main(String[] args) throws Exception{
        Scanner sc=new Scanner(System.in);
        
        int n=sc.nextInt();
        
        /*
        int s=sc.nextInt();
        int m=sc.nextInt();
        int l=sc.nextInt();
        int xl=sc.nextInt();
        int xxl=sc.nextInt();
        int xxxl=sc.nextInt();
        */
        int[] size=new int[6];
        for(int i = 0;i<6;i++) {
        	size[i]=sc.nextInt();
        }
        
        
        int t=sc.nextInt();
        int p=sc.nextInt();
        
        
        // T장씩 최소 몇 묶음을 주문해야 하는지
        int shirts=0;
        for(int i = 0;i<6;i++) {
        	if(size[i]%t==0) {
        		shirts+=size[i]/t;
        	}
        	else {
        		shirts+=size[i]/t + 1;
        	}
        }
        
        // 펜을 최대 몇 묶음 주문할 수 있는지와
        // 펜을 한 자루씩 몇 개 주문하는지
        System.out.println(shirts);
        System.out.println(n/p+" "+n%p);
        
        
        
        
        
        
        
        
    }
        
        

	
}
