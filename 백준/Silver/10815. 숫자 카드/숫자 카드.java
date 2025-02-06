//package ctp;

import java.util.*;


public class Main {
	/*
	public Queue<Integer> solution(int n,int k) {
		
	}*/
	
	public static void main(String[] args) {
		Main T = new Main();
		Scanner sc=new Scanner(System.in);
		
		int n=sc.nextInt();
		Set<Integer> sang=new HashSet<>();
		for(int i = 0;i<n;i++) {
			sang.add(sc.nextInt());
		}
		int m=sc.nextInt();
		Queue<Integer> you=new LinkedList<>();
		for(int i=0;i<m;i++) {
			you.add(sc.nextInt());
		}
		
		for(int element:you) {
			if(sang.contains(element)) System.out.print(1+" ");
			else System.out.print(0+" ");
		}
	}

}
