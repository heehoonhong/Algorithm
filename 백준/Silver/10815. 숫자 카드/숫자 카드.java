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
		List<Integer> you=new ArrayList<>();
		for(int i=0;i<m;i++) {
			you.add(sc.nextInt());
		}
		
		StringBuilder sb=new StringBuilder();
		for(int element:you) {
			if(sang.contains(element)) sb.append("1 ");
			else sb.append("0 ");
		}
		System.out.println(sb.toString().trim());
	}

}
