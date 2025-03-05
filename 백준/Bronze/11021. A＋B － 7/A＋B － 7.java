//package ctp;

import java.util.*;



public class Main {
		
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int[] a=new int[n];
        int[] b=new int[n];
        
        for(int i = 0;i<n;i++) {
        	a[i]=sc.nextInt();
        	b[i]=sc.nextInt();
        }
        for(int i = 0;i<n;i++) {
        	System.out.println("Case #"+(i+1)+": "+(a[i]+b[i]));
        }
        
    }

	
}
