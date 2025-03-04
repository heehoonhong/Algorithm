//package ctp;

import java.util.*;



public class Main {
	
	public static int fibo(int n) {
		
		if(n==1) {
			return 1;
		}
		
		if(n==2) {
			return 2;
		}
		
		int val1=1;
		int val2=2;
		int sum=0;
		
		for(int i = 2;i<n;i++) {
			sum=(val1+val2)%15746;
			val1=val2;
			val2=sum;
		}
		
		return sum;
		
	}

	
	
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n=sc.nextInt();
        //fib=new int[n+1];
        System.out.println(fibo(n));
        
    }

	
}
